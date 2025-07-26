# Prevent selection of content div

## Question

**Geo** asked on 20 Oct 2021

Out of the box the content div (with the k-tabstrip-content class) has a tabindex="0" attribute. Is there a way I can get the TelerikTabStrip to generate this with tabindex="-1" to prevent the div from being selected.

## Answer

**Nadezhda Tacheva** answered on 25 Oct 2021

Hello George, Generally speaking, the reason why we have added tabindex="0" to the <div class="k-tabstrip-content..."> is that it is required for the accessibility of the application. The users who actively use accessibility must be aware that the currently focused element is the content area of the tabstrip. This behavior is mainly due to the way the screen readers work, they notify the user about the focusable elements only. If we decide to remove the tabindex the screen reader will not detect the content area and thus our rendering will not be accessibility friendly which is a major focus of ours. If your desired scenario is to be able to directly focus the content of the TabStripTab on tab press instead of its container, you may try the following approach: <TelerikTabStrip>
<TabStripTab>
<HeaderTemplate>
<div tabindex="0" @onkeydown:stopPropagation
@onkeydown:preventDefault
@onkeydown="@OnKeyDownHandler">
The header of the component.
</div>
</HeaderTemplate>
<Content>
<TelerikTextBox @bind-Value="@theValue" @ref="@TextBoxRef"></TelerikTextBox>
</Content>
</TabStripTab>
<TabStripTab Title="History">
<HeaderTemplate>
<TelerikIcon Icon="clock" />
<strong>Icon and text 2 </strong>
</HeaderTemplate>
<Content>
This is a tab that has a header template and as well as Title parameter.
<br />
Title parameter will not be displayed. Only the Header template will be displayed.
</Content>
</TabStripTab>
<TabStripTab Title="Text only">
This is a tab with Title parameter. If you want to use only text in the header, set the Title parameter only and you can omit the Content tag.
</TabStripTab>
</TelerikTabStrip>

@code { public string theValue { get; set; } public TelerikTextBox TextBoxRef { get; set; } private async Task OnKeyDownHandler ( KeyboardEventArgs e ) { if (e.Key=="Tab" )
{ await TextBoxRef?.FocusAsync();
}
} } However, it is not actually changing the tabindex of the "k-tabstrip-content" div, so in case the user clicks in the container it will get focused and the dotted outline will appear. If you want to cover that scenario, you can add some custom CSS, so the focused container does not have outline: div.k-tabstrip>.k-content:focus, div.k-tabstrip>.k-content.k-state-focused { outline: none;
} I hope you will find the above information useful. Please consider and let us know if the suggested approach will suffice to cover your use case. Thank you in advance! I will be looking forward to hearing form you! Regards, Nadezhda Tacheva

### Response

**George** commented on 25 Oct 2021

Thanks, Nadezhda. Hiding the outline will work for us.
