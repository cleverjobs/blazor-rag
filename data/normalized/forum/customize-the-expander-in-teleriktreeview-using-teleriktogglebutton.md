# Customize the expander in TelerikTreeView using TelerikToggleButton

## Question

**Dus** asked on 06 May 2024

How can I replace the default carat expander of the TelerikTreeView with a customized expander using a TelerikToggleButton? I'd like to toggle between two ISvgIcons as my expand and collapse. What I'm trying to accomplish is very similar to what's being done in this example with RadTreeView and ToggleButton [https://docs.telerik.com/devtools/wpf/controls/radtreeview/styles-and-templates/styling-and-appearance-styling-expander.](https://docs.telerik.com/devtools/wpf/controls/radtreeview/styles-and-templates/styling-and-appearance-styling-expander.)

## Answer

**Nadezhda Tacheva** answered on 07 May 2024

Hi Dustin, You can change the default expand/collapse icons of the TreeView with CSS using the approach listed here: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-change-expand-collapse-icons.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-change-expand-collapse-icons.) The article targets the Grid, but the approach is the same, you just need to use the correct selectors - use your dev tools to inspect the TreeView and find the needed elements. To change the icons on a ToggleButton click, you may apply the CSS conditionally like so: @if (customIconsEnabled)
{ <style> @* your styles here *@</style> } Toggle the customIconsEnabled flag upon the button click to enable the styles. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Dustin** commented on 14 May 2024

Hi Nadezhda, thanks for the response. I didn't state the part about using the TelerikToggleButton very well, what I meant was to incorporate the TelerikToggleButton into TelerikTreeView to toggle between the expand svg and the the collapse svg (something like what the WPF example I attached in my first post). Looking at your TelerikGrid example though, maybe TelerikToggleButton isn't the best way to target the expand and collapse. Could you provide an example of TelerikTreeView with svg icons used for the expand and collapse? I've not been successful adapting the TelerikGrid example to my TelerikTreeView. Thanks, Dustin

### Response

**Nadezhda Tacheva** commented on 15 May 2024

Hi Dustin, As I now understand, you want to use a different icon for the TreeView expand and collapse buttons (elements). Is this correct? This can be achieved with custom CSS as per the approach listed here. I've prepared a runnable sample to demonstrate how: [https://blazorrepl.telerik.com/GyaTlzFJ31Hbm5SM11.](https://blazorrepl.telerik.com/GyaTlzFJ31Hbm5SM11.) My advice is to determine what icons you want to use and render SvgIcon components with those icons. Then, you can use your dev tools to inspect the SVG icons and get their path, so you can use that in the custom CSS. I hope this will help you move forward with the implementation.

### Response

**Dustin** commented on 16 May 2024

Hi Nadezhda, Yes, I'm trying to use different icons for the TreeView expand and collapse elements. And I'm able to achieve what I wanted by following your example. Thank you for posting that. Another question for you on it: I have these Plus and Minus Svgs. <TelerikSvgIcon Icon="@GlobalIcons.Plus"></TelerikSvgIcon> <TelerikSvgIcon Icon="@GlobalIcons.Minus"></TelerikSvgIcon> Which, as you suggested, I'm able to find the paths for using DevTools and get the expand and collapse icons that I want. .custom-icons .k-treeview-toggle .k-svg-icon.k-svg-i-caret-alt-down svg path { d: path("M432 288H400L48 288H16l0-64 32 0 352 0 32 0v64z"); } .custom-icons .k-treeview-toggle .k-svg-icon.k-svg-i-caret-alt-right svg path { d: path("M256 80V48H192V80 224H48 16v64H48 192V432v32h64V432 288H400h32V224H400 256V80z"); } Is it possible to reference my GlobalIcons.Plus and GlobalIcons.Minus directly in the CSS rather than copying the path in? Something like .custom-icons .k-treeview-toggle .k-svg-icon.k-svg-i-caret-alt-down svg path { @GlobalIcons.Minus; } .custom-icons .k-treeview-toggle .k-svg-icon.k-svg-i-caret-alt-right svg path { @GlobalIcons.Plus; } Or can be it be done without the CSS? Something like <TelerikTreeView> <TelerikTreeViewExpand Icon="@GlobalIcons.Plus"></TelerikTreeExpand> <TelerikTreeViewCollapse Icon="@GlobalIcons.Minus"></TelerikTreeCollapse> </TelerikTreeView>

### Response

**Nadezhda Tacheva** commented on 20 May 2024

Hi Dustin, Thank you for the follow-up! I am happy you managed to set up the desired icons in the TreeView. Now, to your next question. UI for Blazor generally allows creating and using a custom SVG Icon Collection. However, the TreeView does not provide an option to specify the desired icons through properties. In a future product version, we will be exploring a way to provide a convenient option for changing the built-in icons. For the time being, the option to change the expand/collapse icons is to use CSS. The styles that I shared strive to change the value of the icons' "path" element. I suspect that the GlobalIcons.Plus and GlobalIcons.Minus that you've mentioned are part of your custom Icon Collection and these objects contain the whole SVG element. If so, it will not be possible to use them in the CSS as you've listed. However, if you want to save the path values in order to reuse them, this will be possible like so: [https://blazorrepl.telerik.com/wIYfcabH583riCSs09.](https://blazorrepl.telerik.com/wIYfcabH583riCSs09.)

### Response

**Dustin** commented on 22 May 2024

Hi Nadezhda, I think that got me everything I needed. Thanks for all the help.
