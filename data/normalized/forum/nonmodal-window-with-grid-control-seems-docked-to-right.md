# NonModal Window with grid control seems docked to right

## Question

**Joh** asked on 28 Feb 2022

Strangest thing. I have a non-modal window control which contains a grid control. For some reason, the window appears to be docked to the right side of the form. I can move the window up and down but if I move it right or left, it just resizes the window width. If I specify a width in px then it is fine. If I specify a width as a percentage then it is docked. Is there a way for the grid to configure the width so it doesn't dock but still takes 100% of the width?

### Response

**Marin Bratanov** commented on 28 Feb 2022

Could you be hitting this flex width issue: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-bootstrap-flex-width-issue?](https://docs.telerik.com/blazor-ui/knowledge-base/grid-bootstrap-flex-width-issue?)

### Response

**John** commented on 28 Feb 2022

Seems like it. I liked the ability to resize the width of the window, too bad it costs the ability to move the window horizontally.

### Response

**Joana** commented on 03 Mar 2022

Hi John, Was our troubleshooting article enough for you to resolve the issue and layout of the Grid and Window components? If no, could you please share a snippet in Repl or project so that we can investigate what styles interfere with our components?

### Response

**John** commented on 03 Mar 2022

If the window width is specified, it does work around the issue though not ideal. Recreated in repl [https://blazorrepl.telerik.com/QGadEnbT24qbDh1G49](https://blazorrepl.telerik.com/QGadEnbT24qbDh1G49)

### Response

**Joana** commented on 08 Mar 2022

Hi John, Thank you for the clarification. I have logged an issue in our
