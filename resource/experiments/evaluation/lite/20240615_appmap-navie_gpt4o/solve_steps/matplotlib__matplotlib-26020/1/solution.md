<change>
    <file change-number-for-this-file="1">lib/mpl_toolkits/axes_grid1/axes_grid.py</file>
    <original line-count="13" no-ellipsis="true"><![CDATA[
def _tick_only(ax, bottom_on, left_on):
    bottom_off = not bottom_on
    left_off = not left_on
    ax.axis["bottom"].toggle(ticklabels=bottom_off, label=bottom_off)
    ax.axis["left"].toggle(ticklabels=left_off, label=left_off)
]]></original>
    <modified no-ellipsis="true"><![CDATA[
def _tick_only(ax, bottom_on, left_on):
    bottom_off = not bottom_on
    left_off = not left_on

    if callable(ax.axis):
        axis_bottom = ax.axis("bottom")
        axis_left = ax.axis("left")
    else:
        axis_bottom = ax.axis["bottom"]
        axis_left = ax.axis["left"]

    axis_bottom.toggle(ticklabels=bottom_off, label=bottom_off)
    axis_left.toggle(ticklabels=left_off, label=left_off)
]]></modified>
</change>