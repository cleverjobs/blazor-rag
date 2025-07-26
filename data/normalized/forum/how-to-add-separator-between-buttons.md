# How to add separator between buttons

## Question

**Mar** asked on 22 Mar 2021

In my button group, I have a set of buttons, where only one button at a time is allowed to be checked. I would like to add a separator between specific buttons, just to make the UI easier to read. I don't see a <ButtonGroupSeparator> or <ButtonGroupSpacer> element. Is adding a CSS style, that increases the left or right padding, to specific <ButtonGroupButton> the best approach?

## Answer

**Svetoslav Dimitrov** answered on 25 Mar 2021

Hello Marc, The ButtonGroup provides a way to group buttons together. If you are using the Bootstrap or Material theme there are no visible borders which are done by the guidelines of both themes. If you would like to visually separate them with a border you can do it by using CSS. If you are using the Bootstrap theme, the below rules would be a suitable base to implement the desire behavior: <style>.k-button-group.k-button ~.k-button { border-left-color: black; margin-inline-start: 0;
}
</style> <TelerikButtonGroup SelectionMode=" @ButtonGroupSelectionMode.Multiple">
<ButtonGroupToggleButton>Bold</ButtonGroupToggleButton>
<ButtonGroupToggleButton>Italic</ButtonGroupToggleButton>
<ButtonGroupToggleButton>Underline</ButtonGroupToggleButton>
</TelerikButtonGroup> Regards, Svetoslav Dimitrov
