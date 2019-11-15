(
    lambda app, layout, dash: setattr(app, "layout", layout)
    or app.callback(
        dash.dependencies.Output(
            component_id="my-div", component_property="children"
        ),
        [
            dash.dependencies.Input(
                component_id="my-input", component_property="value"
            )
        ],
    )(lambda x: f"Hello {x if x is not None else 'there'}!")
    and app.run_server(port=8060, debug=True)
)(
    *(
        lambda dash, html, dcc: (
            dash.Dash(__name__),
            html.Div(
                children=[html.Div(id="my-div"), dcc.Input(id="my-input")]
            ),
            dash,
        )
    )(
        __import__("dash"),
        __import__("dash_html_components"),
        __import__("dash_core_components"),
    )
)
