import pandas as pd
import dash
from dash import dcc, html, dash_table, Input, Output
import plotly.express as px
from datetime import datetime

# Load and prepare data
df = pd.read_csv("C:/Users/hassa/Downloads/CodeHer/Intellectual-Property-Copyright/Debts_Recovery.csv")

# Clean date fields and calculate additional metrics
df["Due Date"] = pd.to_datetime(df["Due Date"], format='%m/%d/%Y')
df["Last Payment Date"] = pd.to_datetime(df["Last Payment Date"], format='%m/%d/%Y')
df['Amount Owed (KES)'] = df['Amount Owed (KES)'].astype(float)
today = pd.to_datetime(datetime.now().date())
df['Days Since Last Payment'] = (today - df['Last Payment Date']).dt.days

# Risk scoring function (enhanced)
def calculate_enhanced_risk(row):
    base_score = 0
    if row['Risk Level'] == 'High': base_score = 80
    elif row['Risk Level'] == 'Medium': base_score = 50
    else: base_score = 20
    
    # Adjust based on days overdue (more days = higher risk)
    days_factor = min(row['Days Overdue'] / 30, 3)  # Cap at 3x multiplier
    # Adjust based on amount (higher amounts = higher risk)
    amount_factor = min(row['Amount Owed (KES)'] / 100000, 2)  # Cap at 2x multiplier
    
    return min(100, base_score * (1 + 0.3 * days_factor + 0.2 * amount_factor))

df['Risk Score'] = df.apply(calculate_enhanced_risk, axis=1)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Advanced Debt Recovery Dashboard"

# Custom CSS styles
styles = {
    'kpi-box': {
        'backgroundColor': '#f8f9fa',
        'borderRadius': '5px',
        'padding': '20px',
        'textAlign': 'center',
        'boxShadow': '0 4px 6px 0 rgba(0,0,0,0.1)',
        'margin': '10px',
        'flex': '1',
        'minWidth': '200px'
    },
    'header': {
        'textAlign': 'center',
        'color': '#2c3e50',
        'marginBottom': '30px'
    }
}

# App Layout
app.layout = html.Div([
    html.H1("Advanced Debt Recovery Dashboard", style=styles['header']),
    
    # KPIs with better styling
    html.Div([
        html.Div([
            html.H4("Total Amount Owed", style={'color': '#7f8c8d'}),
            html.H2(f"{df['Amount Owed (KES)'].sum():,.2f} KES", style={'color': '#e74c3c'})
        ], style=styles['kpi-box']),
        
        html.Div([
            html.H4("High Risk Clients", style={'color': '#7f8c8d'}),
            html.H2(f"{(df['Risk Level'] == 'High').sum()}", style={'color': '#e74c3c'})
        ], style=styles['kpi-box']),
        
        html.Div([
            html.H4("Avg Days Overdue", style={'color': '#7f8c8d'}),
            html.H2(f"{df['Days Overdue'].mean():.1f}", style={'color': '#e74c3c'})
        ], style=styles['kpi-box']),
        
        html.Div([
            html.H4("Recovery Potential", style={'color': '#7f8c8d'}),
            html.H2(f"{df[df['Risk Level'] != 'High']['Amount Owed (KES)'].sum():,.2f} KES", style={'color': '#2ecc71'})
        ], style=styles['kpi-box']),
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center', 'marginBottom': '30px'}),
    
    # First row of charts
    html.Div([
        html.Div([
            dcc.Graph(
                id='risk-distribution',
                figure=px.pie(
                    df, 
                    names="Risk Level", 
                    title="Risk Level Distribution",
                    color_discrete_map={'High':'#e74c3c','Medium':'#f39c12','Low':'#2ecc71'}
                ).update_layout(title_x=0.5)
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(
                id='amount-by-risk',
                figure=px.box(
                    df, 
                    x="Risk Level", 
                    y="Amount Owed (KES)",
                    title="Amount Distribution by Risk Level",
                    color="Risk Level",
                    color_discrete_map={'High':'#e74c3c','Medium':'#f39c12','Low':'#2ecc71'}
                ).update_layout(
                    yaxis_type="log",
                    title_x=0.5
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'}),
    ], style={'marginBottom': '30px'}),
    
    # Second row of charts
    html.Div([
        dcc.Graph(
            id='scatter-plot',
            figure=px.scatter(
                df, 
                x="Days Overdue", 
                y="Amount Owed (KES)",
                color="Risk Score",
                size="Amount Owed (KES)",
                hover_name="Client Name",
                title="Risk Exposure Analysis",
                color_continuous_scale='RdYlGn_r',
                range_color=[0, 100]
            ).update_layout(
                hovermode='closest',
                xaxis_title="Days Overdue",
                yaxis_title="Amount Owed (KES)",
                title_x=0.5
            )
        )
    ], style={'marginBottom': '30px'}),
    
    # Time-based analysis
    html.Div([
        dcc.Graph(
            id='payment-trend',
            figure=px.histogram(
                df, 
                x="Last Payment Date", 
                color="Risk Level",
                title="Payment Activity Timeline",
                color_discrete_map={'High':'#e74c3c','Medium':'#f39c12','Low':'#2ecc71'}
            ).update_layout(
                bargap=0.1,
                xaxis_title="Last Payment Date",
                yaxis_title="Number of Clients",
                title_x=0.5
            )
        )
    ], style={'marginBottom': '30px'}),
    
    # Data table with enhanced features
    html.H3("Client Details", style={'marginTop': '30px', 'textAlign': 'center'}),
    html.Div([
        dcc.Dropdown(
            id='risk-filter',
            options=[
                {'label': 'All Clients', 'value': 'all'},
                {'label': 'High Risk Only', 'value': 'High'},
                {'label': 'Medium Risk Only', 'value': 'Medium'},
                {'label': 'Low Risk Only', 'value': 'Low'}
            ],
            value='all',
            clearable=False,
            style={'width': '300px', 'margin': '0 auto 20px'}
        ),
        dash_table.DataTable(
            id='client-table',
            columns=[
                {"name": "Client", "id": "Client Name"},
                {"name": "Amount Owed (KES)", "id": "Amount Owed (KES)", "type": "numeric", "format": {"specifier": ",.2f"}},
                {"name": "Days Overdue", "id": "Days Overdue"},
                {"name": "Risk Level", "id": "Risk Level"},
                {"name": "Risk Score", "id": "Risk Score", "type": "numeric", "format": {"specifier": ".1f"}},
                {"name": "Last Payment", "id": "Last Payment Date"},
                {"name": "Due Date", "id": "Due Date"}
            ],
            page_size=15,
            filter_action="native",
            sort_action="native",
            sort_by=[{"column_id": "Risk Score", "direction": "desc"}],
            style_table={'overflowX': 'auto', 'margin': '0 auto', 'maxWidth': '1200px'},
            style_cell={
                'textAlign': 'left',
                'padding': '10px',
                'whiteSpace': 'normal',
                'height': 'auto',
                'border': '1px solid #eee'
            },
            style_header={
                'backgroundColor': '#2c3e50',
                'color': 'white',
                'fontWeight': 'bold'
            },
            style_data_conditional=[
                {
                    'if': {'filter_query': '{Risk Level} = "High"'},
                    'backgroundColor': '#ffebee',
                    'color': '#c62828'
                },
                {
                    'if': {'filter_query': '{Risk Level} = "Medium"'},
                    'backgroundColor': '#fff8e1'
                },
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                }
            ]
        )
    ], style={'marginBottom': '50px'})
])

# Callback for table filtering
@app.callback(
    Output('client-table', 'data'),
    Input('risk-filter', 'value')
)
def update_table(risk_level):
    if risk_level == 'all':
        return df.to_dict('records')
    else:
        filtered_df = df[df['Risk Level'] == risk_level]
        return filtered_df.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)