# Splitter Width

## Question

**Dar** asked on 14 Sep 2021

How can I change the width of the Splitter itself?

## Answer

**Nikolas** answered on 16 Sep 2021

Hello Daryl, If you are talking about the splitter div for resizing, I did it with CSS, could not get it working with other methods. .k-splitbar-horizontal { width: 15px!important;
}.k-splitbar-vertical { height: 15px!important;
} If it's the size of the pane, then here is the docs link: [https://docs.telerik.com/blazor-ui/components/splitter/overview](https://docs.telerik.com/blazor-ui/components/splitter/overview) Best regards, Nikolas

### Response

**Daryl** commented on 16 Sep 2021

This works for me. Thank you!

### Response

**Dimo** answered on 16 Sep 2021

Hi Daryl, The Splitter tag exposes Width and Height attributes for setting dimensions in different units. In case you are asking about dynamic resizing, this is possible as well. <p> Set the Splitter width here (@Min.ToString() - @Max.ToString()): <TelerikNumericTextBox Min="@Min" Max="@Max" Decimals="0" @bind-Value="@SpliterWidth" /> </p> <TelerikSplitter Orientation="SplitterOrientation.Horizontal" Height="200px" Width="@( Math.Max(SpliterWidth, Min) + " px " )"> <SplitterPanes> <SplitterPane Collapsible="true"> Pane 1 </SplitterPane> <SplitterPane Collapsible="true"> Pane 2 </SplitterPane> </SplitterPanes> </TelerikSplitter> @code {
int SpliterWidth=400;
int Min=100;
int Max=1000;
} Regards, Dimo Progress Telerik
