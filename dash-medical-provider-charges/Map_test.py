import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('hospital_rating.csv')
#df.head()
#
# #df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)
# df['text']= df['Facility Name'] + '\n' + df['Hospital overall rating'].astype(str)
#
#
# scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
#     [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]



app = dash.Dash(
    __name__,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no",
        }
    ],
)
server = app.server

app.config["suppress_callback_exceptions"] = True



# data = [ dict(
#         type = 'scattergeo',
#         locationmode = 'USA-states',
#         lon = df['lon'],
#         lat = df['lat'],
#         text = df['text'],
#         mode = 'markers',
#         marker = dict( #style layout of markers on map
#             size = 4,
#             opacity = 0.7,
#             reversescale = True,
#             autocolorscale = False,
#             symbol = 'circle',
#             line = dict(
#                 width=1,
#                 color='rgba(102, 102, 102)'
#             ),
#             colorscale = scl,
#             cmin = 0,
#             color = df['Hospital overall rating'],
#             cmax = df['Hospital overall rating'].max(),
#             colorbar=dict(
#                 title="Hospital Rating"
#             )
#         ))]
#
# layout = dict(
#         title = 'Overall Hospital Ratings<br>(Hover for hospital names)',
#         colorbar = True,
#         geo = dict(
#             scope='usa',
#             projection=dict( type='albers usa' ),
#             showland = True,
#             landcolor = "rgb(250, 250, 250)",
#             subunitcolor = "rgb(217, 217, 217)",
#             countrycolor = "rgb(217, 217, 217)",
#             countrywidth = 0.5,
#             subunitwidth = 0.5
#         ),
#     )
#
# fig = dict( data=data, layout=layout )

### app.py stuff below
# Plotly mapbox token
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNqdnBvNDMyaTAxYzkzeW5ubWdpZ2VjbmMifQ.TXcBE-xg9BFdV2ocecc_7g"
state_map = {
    "AK": "Alaska",
    "AL": "Alabama",
    "AR": "Arkansas",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DC": "District of Columbia",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming",
}

state_list = list(state_map.keys())
cost_metric = [5,4,3,2,1]

def build_upper_left_panel():
    return html.Div(
        id="upper-left",
        className="six columns",
        children=[
            html.P(
                className="section-title",
                children="Choosing hospital test",
            ),
            html.Div(
                className="control-row-1",
                children=[
                    html.Div(
                        id="state-select-outer",
                        children=[
                            html.Label("Select a State"),
                            dcc.Dropdown(
                                id="state-select",
                                options=[{"label": i, "value": i} for i in state_list],
                                value=state_list[1],
                            ),
                        ],
                    ),
                    html.Div(
                        id="select-metric-outer",
                        children=[
                            html.Label("Choose a Rating"),
                            dcc.Dropdown(
                                id="metric-select",
                                options=[{"label": i, "value": i} for i in cost_metric],
                                value=cost_metric[0],
                            ),
                        ],
                    ),
                ],
            ),
            # html.Div(
            #     id="region-select-outer",
            #     className="control-row-2",
            #     children=[
            #         html.Label("Pick a Region"),
            #         html.Div(
            #             id="checklist-container",
            #             children=dcc.Checklist(
            #                 id="region-select-all",
            #                 options=[{"label": "Select All Regions", "value": "All"}],
            #                 values=["All"],
            #             ),
            #         ),
            #         html.Div(
            #             id="region-select-dropdown-outer",
            #             children=dcc.Dropdown(
            #                 id="region-select",
            #                 options=[{"label": i, "value": i} for i in init_region],
            #                 value=init_region[:4],
            #                 multi=True,
            #                 searchable=True,
            #             ),
            #         ),
            #     ],
            # ),
            # html.Div(
            #     id="table-container",
            #     className="table-container",
            #     children=[
            #         html.Div(
            #             id="table-upper",
            #             children=[
            #                 html.P("Hospital Charges Summary"),
            #                 dcc.Loading(children=html.Div(id="cost-stats-container")),
            #             ],
            #         ),
            #         html.Div(
            #             id="table-lower",
            #             children=[
            #                 html.P("Procedure Charges Summary"),
            #                 dcc.Loading(
            #                     children=html.Div(id="procedure-stats-container")
            #                 ),
            #             ],
            #         ),
            #     ],
            # ),
        ],
    )


#MAP stuff
def generate_geo_map(geo_data, selected_metric, region_select, procedure_select):
    # filtered_data = geo_data[
    #     geo_data["Hospital Referral Region (HRR) Description"].isin(region_select)
    # ]

    colors = ["#21c7ef", "#76f2ff", "#ff6969", "#ff1717"]

    hospitals = []

    lat = df["lat"].tolist()
    lon = df["lon"].tolist()
    #average_covered_charges_mean = filtered_data[selected_metric]["mean"].tolist()
    #regions = filtered_data["Hospital Referral Region (HRR) Description"].tolist()
    provider_name = df["Facility Name"].tolist()

    # Cost metric mapping from aggregated data

    # cost_metric_data = {}
    # cost_metric_data["min"] = filtered_data[selected_metric]["mean"].min()
    # cost_metric_data["max"] = filtered_data[selected_metric]["mean"].max()
    # cost_metric_data["mid"] = (cost_metric_data["min"] + cost_metric_data["max"]) / 2
    # cost_metric_data["low_mid"] = (
    #     cost_metric_data["min"] + cost_metric_data["mid"]
    # ) / 2
    # cost_metric_data["high_mid"] = (
    #     cost_metric_data["mid"] + cost_metric_data["max"]
    # ) / 2

    for i in range(len(lat)):
        #val = average_covered_charges_mean[i]
        #region = regions[i]
        provider = provider_name[i]

        # if val <= cost_metric_data["low_mid"]:
        #     color = colors[0]
        # elif cost_metric_data["low_mid"] < val <= cost_metric_data["mid"]:
        #     color = colors[1]
        # elif cost_metric_data["mid"] < val <= cost_metric_data["high_mid"]:
        #     color = colors[2]
        # else:
        #     color = colors[3]

        # selected_index = []
        # if provider in procedure_select["hospital"]:
        #     selected_index = [0]

        hospital = go.Scattermapbox(
            lat=[lat[i]],
            lon=[lon[i]],
            mode="markers",
            marker=dict(
                color=color,
                showscale=True,
                colorscale=[
                    [0, "#21c7ef"],
                    [0.33, "#76f2ff"],
                    [0.66, "#ff6969"],
                    [1, "#ff1717"],
                ],
                cmin= df['Hospital overall rating'].min(),#cost_metric_data["min"],
                cmax= df['Hospital overall rating'].max(),#cost_metric_data["max"],
                size=10
                #* (1 + (val + cost_metric_data["min"]) / cost_metric_data["mid"]),
                ,
                colorbar=dict(
                    x=0.9,
                    len=0.7,
                    title=dict(
                        text="Average Cost",
                        font={"color": "#737a8d", "family": "Open Sans"},
                    ),
                    titleside="top",
                    tickmode="array",
                    #tickvals=[cost_metric_data["min"], cost_metric_data["max"]],
                    # ticktext=[
                    #     "${:,.2f}".format(cost_metric_data["min"]),
                    #     "${:,.2f}".format(cost_metric_data["max"]),
                    # ],
                    ticks="outside",
                    thickness=15,
                    tickfont={"family": "Open Sans", "color": "#737a8d"},
                ),
            ),
            opacity=0.8,
            selectedpoints=selected_index,
            selected=dict(marker={"color": "#ffff00"}),
            customdata=[(provider, region)],
            hoverinfo="text",
            text=provider
            + "<br>"
            + region
            + "<br>Average Procedure Cost:"
            + " ${:,.2f}".format(val),
        )
        hospitals.append(hospital)

    layout = go.Layout(
        margin=dict(l=10, r=10, t=20, b=10, pad=5),
        plot_bgcolor="#171b26",
        paper_bgcolor="#171b26",
        clickmode="event+select",
        hovermode="closest",
        showlegend=False,
        mapbox=go.layout.Mapbox(
            accesstoken=mapbox_access_token,
            bearing=10,
            center=go.layout.mapbox.Center(
                lat=filtered_data.lat.mean(), lon=filtered_data.lon.mean()
            ),
            pitch=5,
            zoom=5,
            style="mapbox://styles/plotlymapbox/cjvppq1jl1ips1co3j12b9hex",
        ),
    )

    return {"data": hospitals, "layout": layout}








app.layout = html.Div(
    className="container scalable",
    children=[
        html.Div(
            id="banner",
            className="banner",
            children=[
                html.H6("Dash Clinical Analytics"),
                html.Img(src=app.get_asset_url("plotly_logo_white.png")),
            ],
        ),
        html.Div(
            id="upper-container",
            className="row",
            children=[
                build_upper_left_panel(),
                html.Div(
                    id="geo-map-outer",
                    className="six columns",
                    children=[
                        html.P(
                            id="map-title",
                            children="Medicare Provider Charges in the State of {}".format(
                                state_map[state_list[0]]
                            ),
                        ),
                        html.Div(
                            id="geo-map-loading-outer",
                            children=[
                                dcc.Loading(
                                    id="loading",
                                    children=dcc.Graph(
                                        id="geo-map",
                                        figure={
                                            "data": [],
                                            "layout": dict(
                                                plot_bgcolor="#171b26",
                                                paper_bgcolor="#171b26",
                                            ),
                                        },
                                    ),
                                )
                            ],
                        ),
                    ],
                ),
            ],
        ),
        # html.Div(
        #     id="lower-container",
        #     children=[
        #         dcc.Graph(
        #             id="procedure-plot",
        #             figure=generate_procedure_plot(
        #                 data_dict[state_list[1]], cost_metric[0], init_region, []
        #             ),
        #         )
        #     ],
        # ),
    ],
) #layout for this plot
#
# def build_upper_left_panel():
#     return html.Div(
#         id="upper-left",
#         className="six columns",
#         children=[
#             html.P(
#                 className="section-title",
#                 children="Choose hospital on the map or procedures from the list below to see costs",
#             ),
#             html.Div(
#                 className="control-row-1",
#                 children=[
#                     html.Div(
#                         id="state-select-outer",
#                         children=[
#                             html.Label("Select a State"),
#                             dcc.Dropdown(
#                                 id="state-select",
#                                 options=[{"label": i, "value": i} for i in state_list],
#                                 value=state_list[1],
#                             ),
#                         ],
#                     ),
#                     html.Div(
#                         id="select-metric-outer",
#                         children=[
#                             html.Label("Choose a Cost Metric"),
#                             dcc.Dropdown(
#                                 id="metric-select",
#                                 options=[{"label": i, "value": i} for i in cost_metric],
#                                 value=cost_metric[0],
#                             ),
#                         ],
#                     ),
#                 ],
#             ),
#             html.Div(
#                 id="region-select-outer",
#                 className="control-row-2",
#                 children=[
#                     html.Label("Pick a Region"),
#                     html.Div(
#                         id="checklist-container",
#                         children=dcc.Checklist(
#                             id="region-select-all",
#                             options=[{"label": "Select All Regions", "value": "All"}],
#                             values=["All"],
#                         ),
#                     ),
#                     html.Div(
#                         id="region-select-dropdown-outer",
#                         children=dcc.Dropdown(
#                             id="region-select",
#                             options=[{"label": i, "value": i} for i in init_region],
#                             value=init_region[:4],
#                             multi=True,
#                             searchable=True,
#                         ),
#                     ),
#                 ],
#             ),
#             html.Div(
#                 id="table-container",
#                 className="table-container",
#                 children=[
#                     html.Div(
#                         id="table-upper",
#                         children=[
#                             html.P("Hospital Charges Summary"),
#                             dcc.Loading(children=html.Div(id="cost-stats-container")),
#                         ],
#                     ),
#                     html.Div(
#                         id="table-lower",
#                         children=[
#                             html.P("Procedure Charges Summary"),
#                             dcc.Loading(
#                                 children=html.Div(id="procedure-stats-container")
#                             ),
#                         ],
#                     ),
#                 ],
#             ),
#         ],
#     )

# app.layout  = html.Div([
#     dcc.Graph(id='graph', figure=fig)
# ])

if __name__ == '__main__':
    app.run_server(debug=True)
