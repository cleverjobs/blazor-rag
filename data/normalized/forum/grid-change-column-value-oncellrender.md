# Grid change column value OnCellRender

## Question

**Jef** asked on 04 Mar 2021

I use Telerik Blazor Grid component and want to change column value when it is databinding. Is it possible to change original databinding value using OnCellRender handler?

### Response

**Michal** commented on 23 Aug 2022

Hello, i would like to ask how to use Cell Template, or OnCellRender when you want to chage the CELL background color NOT by the css class. All examples are arround css SomeStyle{ background:clred}, but what if you have color in hex/int/ inline style format? Looking for something like this: ... OnCellRender="@((e)=> e.Style="background-color:((ModelABC)e.Item).argbcolor ")">... Problem is with FULL 100% width and height of the cell content. Setting padding on grid level is "no-go" for just conditionally changing table cell "style". Setting the height:1px; instead of 100% inside nopaddingcell style is nice css trick, but has another side d-effects. :) Not working(all combinations with template, onrender found on examples and forum yet): <style> .nopaddingcell { padding: 0 !important; height:100%; } /* .k-grid-table td .nopaddingcell { height: 100%; /*height:1px;*/ padding: 0px !important; } */ </style> <GridColumn Field="..." Title="P" Width="30px" OnCellRender="@((e)=> e.Class="nopaddingcell"> <Template> @{
var it=context as ModelABC; <div class="nopaddingcell" style=@GetColorFromValue(it. argbcolor )> @it.txtvalue </div> } </Template> </GridColumn> Thanks for any ideas

### Response

**Dimo** commented on 24 Aug 2022

Michal - I assume that CSS classes don't work or you, because you have a lot of different colors. Alas, there is no exposed API to apply background color style at cell level, UNLESS you use a row template. This comes with its caveats though, which are documented. So my suggestion is - generate CSS classes for all the background colors that you need to support, if feasible. Alternatively, remove the cell paddings from this specific column and add the padding back to an inner element inside the column template. Here is a runnable REPL test page that shows this in action.

### Response

**Michal** commented on 24 Aug 2022

Unfortunately even the example with column template and padding is not working well. If the rows are even height-sized, padding is not an option. - generating ALL existing colors to CSS classes will be huge list :) . Anything can arrive in data as color - unkown combinations. Iam hoped for something like in the asp GridView and AjaxRadGrid, styling. Most of the time all these scenarions are common: 1 - change cell back color/style=no sollution yet. Rebuilding whole grid row template because of few columns/cells/styles ... oh. 2 - change whole cell content back color/style=this is what you get in example(cell template), partly working with FIXED dimensions 3 - change content color/style=working as expected <TelerikGrid Data="@GridData" TItem="@Product" RowHeight="60"> .... Any plans adding to the OnRenderCell something like "e.AddStyle=....' ? Have a nice day Dimo

### Response

**Dimo** commented on 24 Aug 2022

We have a feature request for inline styles, but it's not very popular yet (I voted on your behalf). So this is what I can offer at this point (apart from the mentioned row template): For scenarios with RowHeight or predictable row height in general, use my previous approach, but with some more CSS. For scenarios with unpredictable row height, consider additional CSS trickery.

### Response

**Michal** commented on 29 Aug 2022

Thank You for your time Dimo, seccond scenario helped a lot, lets see how it perform in real world :) Based on that css trickery iam goiong to prepare inherited definition of GridColumn to something reusable like: <GridColumnExt Field="Data" BackColor=@((e)=> e.Value=e.it.BackColorDefintion)> </GridColumnExt> or <GridColumnExt Field="Data" OnCellRender=@((e)=> e.BackColor=e.Item....)> </GridColumnExt>

## Answer

**Marin Bratanov** answered on 04 Mar 2021

Hi Jeff, The OnCellRender event is used only for appearance. To change what the cell displays, you need to use the corresponding template - like the cell template or the editor template, depending on what you are after. Regards, Marin Bratanov

### Response

**Jeff** answered on 04 Mar 2021

Thank you Marin. I use column template and the value of the column can be changed. I have another question: how to display column's value on the popup edit window when using column template?

### Response

**Jeff** answered on 05 Mar 2021

I found that the EditorTemplate can display value in the popup edit window.
