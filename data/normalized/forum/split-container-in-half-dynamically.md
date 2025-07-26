# Split container in half dynamically

## Question

**Cip** asked on 21 Sep 2021

Hi everybody, What I would like to achieve is to split a container in 2 halfs, then after selecting one of the two halfs to have the posibility to split the selected half agin in other two halfs, and so on. I was thinking to use the Splitter component for this kind of things having two buttons: one for splitting vertically, and one for splitting horizontally which when one is pressed do the split of the selected container, but I can't understand how can I do this because in all your examples the splitters are already defined. How can this be done dynamically? Can anyone help me? Best regards. Cipri

## Answer

**Nadezhda Tacheva** answered on 24 Sep 2021

Hello Ciprian, You can use some conditional markup for the nested Splitters and render them based on a flag that you can toggle on a button click. You can define another flag to control the Splitter orientation. The example below demonstrates the described approach. You can use it as a reference and extend it to match your application needs. <TelerikButton OnClick="@SplitRightHorizontally"> Split Right Pane Horizontally </TelerikButton> <TelerikButton OnClick="@SplitRightVertically"> Split Right Pane Vertically </TelerikButton> <TelerikSplitter Width="600px" Height="600px"> <SplitterPanes> <SplitterPane Size="200px"> <div> left sidebar </div> </SplitterPane> <SplitterPane> @if (isRightPaneSplit)
{ <TelerikSplitter Class="k-pane-flex" Width="100%" Height="100%" Orientation="@(horizontalSplit? SplitterOrientation.Horizontal : SplitterOrientation.Vertical)"> <SplitterPanes> <SplitterPane Size="40%"> <div> First child pane content </div> </SplitterPane> <SplitterPane> <div> Second child pane content </div> </SplitterPane> </SplitterPanes> </TelerikSplitter> } </SplitterPane> </SplitterPanes> </TelerikSplitter> @code{
public bool isRightPaneSplit { get; set; }

public bool horizontalSplit { get; set; }

void SplitRightHorizontally()
{
isRightPaneSplit=true;

horizontalSplit=true;
}

void SplitRightVertically()
{
isRightPaneSplit=true;
}

} Regards, Nadezhda Tacheva Progress Telerik
