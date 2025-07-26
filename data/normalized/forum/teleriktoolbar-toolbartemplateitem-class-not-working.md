# TelerikToolbar ToolBarTemplateItem Class Not Working

## Question

**Jos** asked on 21 Apr 2022

We recently made the update from version 2.* to 3.1.0 and then 3.2.0. I'm unsure when and where the change occurred but we are now having problems with the items visual display. Previously, we had 2 ToolBarTemplateItem's setup like so: <TelerikToolBar Class="toolbar-size">

<ToolBarTemplateItem>
<TelerikMultiSelect
Class="font-size-12 ml-5 bg-light-transparent h-auto" Data="@Data" Value="@ChosenModelNames" TextField="@nameof(TreeView.Text)" ValueField="@nameof(TreeView.Id)" Placeholder="Select Data" ValueChanged="@((List<string> args)=> ChosenModelsChanged(args))" Width="auto" ItemHeight="25" FillMode="@ThemeConstants.DropDownList.FillMode.Outline" Rounded="@ThemeConstants.DropDownList.Rounded.Small" Size="@ThemeConstants.DropDownList.Size.Large">
<ItemTemplate>
@{ var ctx=context as TreeView;
}
@ctx.DisplayName @ctx.Name
</ItemTemplate>
</TelerikMultiSelect>
</ToolBarTemplateItem>

<ToolBarTemplateItem>
<div class="mt-4 ml-2 w-100">
<TelerikRangeSlider
@bind-StartValue="@StartValue" @bind-EndValue="@EndValue" Min="0" Max="25" SmallStep="@SmallStep" LargeStep="@LargeStep" Width="95%" OnChange="@(args=> TimeUpdateHandler())" TickPosition="@SliderTickPosition.Before">
<LabelTemplate>
<div class="time-slider-text">
@(GetRangeDate(context).ToString( "htt" ))
</div>
</LabelTemplate>
</TelerikRangeSlider>
</div>

</ToolBarTemplateItem>

</TelerikToolBar> This now adds div elements to the dom that I don't believe were there before. I then attempted to use <ToolBarTemplateItem Class="myClass"> but the class doesn't actually go into that div or anywhere else that I can see.

## Answer

**Hristian Stefanov** answered on 26 Apr 2022

Hi Joshua, UI for Blazor 3.0 introduced significant changes in our components, including their rendering. Here is the relevant documentation that we updated together with the release: Release Notes (see also - 3.1.0 and 3.2.0 notes) Breaking Changes Please use the examples from above as a reference to configure all needed components in the actual updated project. It is important for us to know that the above resources are easy to find and follow. Let us know if you expected this information elsewhere, or have suggestions about the content. Additionally, if the project theme comes from somewhere locally, you can rebuild the theme with the latest version. If the problem is still there after following the above articles, may I kindly ask you to send us a small runnable project that shows the behavior? This will allow me to investigate further and suggest next steps. Thank you. Regards, Hristian Stefanov Progress Telerik
