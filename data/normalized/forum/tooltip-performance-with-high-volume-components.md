# Tooltip performance with high volume components

## Question

**Emm** asked on 13 Oct 2023

So we are building a component comprised of a high number of child components (think of a page with lots of controls on it). Ideally I want to use the TelerikTooltip for every child control component to display a tooltip on hover. However when we get above 140 child components the initial load performance of the ui gets significantly slower. I am testing with a baseline of 500 child components and using the TelerikTooltip delays the render by about 13 seconds when compared to my own attempts at a tooltip (or not using it at all). Are there any known performance tricks for the TelerikTooltip or anything in the pipeline for performance improvements with the TelerikTooltip? Code snippet below where ComponentVM.ControlVMs has 500 objects: foreach (IControlVM nextControl in ComponentVM.ControlVMs)
{
ControlName=nextControl.FormControlVM.FormControl.GetType().Name;
<TelerikTooltip TargetSelector=".tooltip-target" Class="menu-tooltip" />

<div style="position:absolute;
z-index:@nextControl.FormControlVM.ZIndex;
border-radius:2px; border-width:2px; border-color:red;
width:@string.Format(" { 0 }cm ", nextControl.FormControlVM.Width);
height:@string.Format(" { 0 }cm ", nextControl.FormControlVM.Height);
left:@string.Format(" { 0 }cm ", nextControl.FormControlVM.CanvasLeft);
top:@string.Format(" { 0 }cm ", nextControl.FormControlVM.CanvasTop);
overflow:hidden;">

@if (ControlRazors.ContainsKey(ControlName))
{
Dictionary<string, object> controlParams=new Dictionary<string, object>()
{
{ nameof (ComponentVM), nextControl}
};
<DynamicComponent Type="ControlRazors[ControlName]" Parameters="controlParams" />

}

</div>
}

## Answer

**Georgi** answered on 18 Oct 2023

Hi, Emmett, Yes, there is a trick to improve performance for the TelerikTooltip. It is possible to use a single ToolTip instance for multiple elements, which will drastically increase performance. I have prepared a REPL example to demonstrate the difference. Let me know if additional help is needed. Regards, Georgi Progress Telerik
