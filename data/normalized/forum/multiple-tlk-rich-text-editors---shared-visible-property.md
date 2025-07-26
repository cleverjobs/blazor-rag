# Multiple Tlk Rich Text Editors - shared Visible property

## Question

**Cat** asked on 22 Jul 2021

Hello! Consider the code bellow. I have an @ondblclick event on a card that sets a boolean value which in turns controls the visible property of a Telerik RTE inside a foreach loop. The problem is when I double click on card, all the RTEs become visible. How can I control the dblclick event to set the Visible property of the RTE inside the card I dblclick? Any hint will do. I dont know if I am making any sense, but I can provide additional details if needed. @foreach ( var chapters in leaseContractDefaultTemplateChapters.OrderBy(s=> s.DisplayOrder))
{
<MudContainer Fixed="true">
<MudPaper Height="auto" Width="auto">
<MudCard @ondblclick="@OnChapterCardDoubleClick">
<MudCardHeader>
<CardHeaderContent>
<MudText Class="d-flex" Typo="Typo.h6">@chapters.Name</MudText>
</CardHeaderContent>
<CardHeaderActions>
<MudIconButton OnClick="@(async ()=> await GetComputedTemplateChapter())" Icon="@Icons.Material.Outlined.Functions" />
<MudIconButton OnClick="@OnSaveChapterClick" Icon="@Icons.Material.Filled.Save" Color="Color.Success" />
</CardHeaderActions>
</MudCardHeader>
<MudCardContent>
@if (rteVisible)
{
<TelerikEditor @ref="chapterEditor" @bind-Value="@chapters.HtmlString" Tools="@Tools" Height="300px">
</TelerikEditor>
} else {
@((MarkupString)chapters.HtmlString)
}
</MudCardContent>
</MudCard>
</MudPaper>
</MudContainer>
}

## Answer

**Marin Bratanov** answered on 22 Jul 2021

Hi Catalin, There seems to be only one flag that controls the visibility of all components in the loop, which means it will affect all instances the loop renders. If you want control on a per-instance basis, you should add the flag to the descriptor model over which you make the loop, and toggle only the flag for that specific object reference. This is not stemming from the Telerik component, and we cannot influence it, it is the way the framework operates. Regards, Marin Bratanov Progress Telerik
