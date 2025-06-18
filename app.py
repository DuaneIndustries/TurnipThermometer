import plotly.graph_objects as go
from PIL import Image
import io
import plotly.io as pio

# Load your logo (adjust path or use with open if local)
logo_path = "images/radish_overlay3.png"

with open(logo_path, "rb") as f:
   logo_data = f.read()
# Parameters
goal_amount = 600000
final_raised = 600000
steps = 20
step_amount = final_raised // steps
cheat_base = 1/6
bar_max=2/3
# Frames for animation
frames = []
for i in range(steps + 1):
   current_amount = i * step_amount
   fill_percent = current_amount / goal_amount
   cheat_height = fill_percent * bar_max
   frames.append(go.Frame(
       data=[
           go.Bar(
               x=["Fundraising"],
               y=[cheat_height],
               marker=dict(color="rgba(160, 43, 34, 0.6)"),
               width=1.0,
               base=cheat_base
           )
       ],
       name=str(current_amount),
       layout=go.Layout(
           annotations=[
               dict(
                   text=f"${current_amount:,} raised",
                   x=0.5,
                   y=1.05,
                   xref="paper",
                   yref="paper",
                   showarrow=False,
                   font=dict(size=24)
               )
           ]
       )
   ))
# Initial bar chart
fig = go.Figure(
   data=[
       go.Bar(
           x=["Fundraising"],
           y=[0],
           marker=dict(color="rgba(160, 43, 34, 0.6)"),
           width=1.0,
           base=0
       )
   ],
   frames=frames
)
# Add the logo on top
fig.add_layout_image(
   dict(
       source=Image.open(io.BytesIO(logo_data)),
       xref="paper", yref="paper",
       x=0, y=1,
       sizex=1, sizey=1,
       xanchor="left", yanchor="top",
       sizing="stretch",
       layer="above"
   )
)
# Frame/logo overlay (top layer)
fig.add_layout_image(
   dict(
       source=Image.open("images/radish_overlay3.png"),  # Add your image file path here
       xref="paper", yref="paper",
       x=0, y=1,
       sizex=1, sizey=1,
       xanchor="left", yanchor="top",
       sizing="stretch",  # or "contain" to keep proportions
       layer="above"
   )
)

# Play button and layout
fig.update_layout(
   updatemenus=[dict(
       type="buttons",
       showactive=False,
       buttons=[dict(label="Play",
                     method="animate",
                     args=[None, {"frame": {"duration": 300, "redraw": True},
                                  "fromcurrent": True,
                                  "mode": "immediate"}])]
   )],
   annotations=[
       dict(
           text="$0 raised",
           x=0.5,
           y=1.05,
           xref="paper",
           yref="paper",
           showarrow=False,
           font=dict(size=24)
       )
   ],
   margin=dict(l=0, r=0, t=40, b=0),
   xaxis=dict(visible=False),
   yaxis=dict(range=[0, 1], visible=False),
   width=500,
   height=500
)
fig.show()



# fig.update_layout(
#    annotations=[
#        dict(
#            text="$0 raised",
#            x=0.5,
#            y=1.05,
#            xref="paper",
#            yref="paper",
#            showarrow=False,
#            font=dict(size=24)
#        )],
#    margin=dict(l=0, r=0, t=40, b=0),
#    xaxis=dict(visible=False),
#    yaxis=dict(range=[0, 1], visible=False),
#    width=500,
#    height=700,
#    transition=dict(duration=0),
# )
# # Set frame transition on load
# fig.update_layout(
#    updatemenus=[],
#    sliders=[],
# )
# # Show figure with auto animation (works in HTML export or in-browser)
# fig.show(animation_opts=dict(
#    frame=dict(duration=300, redraw=True),
#    transition=dict(duration=0),
#    mode='immediate'
# ))

# Export to HTML with animation auto-playing
# pio.write_html(
#    fig,
#    file="fundraising_chart.html",
#    auto_open=True,
#    include_plotlyjs="cdn",
#    full_html=True,
#    config={"displayModeBar": False},
#    animation_opts=dict(
#        frame=dict(duration=300, redraw=True),
#        transition=dict(duration=0),
#        mode="immediate"
#    )
# )