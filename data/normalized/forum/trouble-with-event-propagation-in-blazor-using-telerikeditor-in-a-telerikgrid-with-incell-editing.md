# Trouble with Event Propagation in Blazor using Telerikeditor in a Telerikgrid with Incell editing

## Question

**Fat** asked on 16 Apr 2024

Hello everyone, I am experiencing an issue with my Blazor application and am seeking advice or solutions from anyone who might have had the same issue. When interacting with the Telerik Editor within a Telerik Grid, clicking inside the editor unexpectedly exits the edit mode. This seems to be linked to event propagation issues, where clicking the editor triggers a propagation that causes the grid to exit edit mode. Error Messages: When my issue triggers, I also see the following error in the console: Uncaught TypeError: Cannot read properties of null (reading 'state') This occurs within the telerik-blazor.js script and seems related to handling state changes or events. I already looked trough Troubleshooting but removing all "StateHasChanged" didn't solve the issue. What I've Tried: Implemented JavaScript to stop event propagation using event.stopPropagation() within various event handlers (click, mousedown, etc.). Checked that the event handlers are correctly assigned and that the JavaScript is initialized at the correct life cycle phase in Blazor (OnAfterRenderAsync). Removed any redundant StateHasChanged() calls as per Telerik's recommendations to prevent unnecessary re-rendering and potential race conditions. Code: The Telerikgrid with the Telerikeditor: <TelerikGrid Data="ProzessSubPosListe" EditMode="@GridEditMode.Incell" OnUpdate="@UpdateHandlerProzessPos" OnDelete="@DeleteHanlderProzessPos" Size="@ThemeConstants.Grid.Size.Small" PageSize="100" Sortable="true" Pageable="false" Resizable="true">
<GridColumns>
<GridColumn Field="@nameof(ProzessPosClass.Nr)" Title="Nr" Width="10%"></GridColumn>
<GridColumn Field="@nameof(ProzessPosClass.Title)" Title="Thema" Width="20%"></GridColumn>
<GridColumn Field="@nameof(ProzessPosClass.ProzessContent)" Title="Beschreibung" Width="20%">
<EditorTemplate Context="dataItem">
<div @onclick:stopPropagation="true" @onclick:preventDefault="true">
@{ var item=dataItem as ProzessPosClass;
<TelerikEditor @bind-Value="@item.ProzessContent" Width="650px" Height="400px"></TelerikEditor>
}
</div>
</EditorTemplate>
</GridColumn>
<GridCommandColumn Context="Journal" Width="100px">
<GridCommandButton Command="Save" Icon="@(" save ")" ShowInEdit="true"></GridCommandButton>
<GridCommandButton Command="Delete" Icon="@(" trash ")"></GridCommandButton>
<GridCommandButton Command="Cancel" Icon="@(" cancel ")" ShowInEdit="true"></GridCommandButton>
</GridCommandColumn>
</GridColumns>
<NoDataTemplate>
<strong>Kein Prozessschritt vorhanden</strong>
</NoDataTemplate>
</TelerikGrid> OnAfterRenderAsync Method to call the Javascript function. protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (firstRender)
{ await JSRuntime.InvokeVoidAsync( "setupEditorEventHandling" );
}
} My Javascript inside of _Layout.cshtml trying to resolve the issue: <script> function setupEditorEventHandling ( ) { console. log ( "Setup editor event handling" ); document. addEventListener ( 'click', function ( event ) { try { var editor=event. target. closest ( '.k-editor.telerik-blazor' ); if (editor) {
event. stopPropagation ();
}
} catch (error) { console. error ( 'Error handling editor click:', error);
}
}, true );
}
</script> How the issue looks like: Has anyone encountered similar issues with event handling in Blazor applications using that setup? Any insights or suggestions would be greatly appreciated.

### Response

**Lee** commented on 06 Jun 2024

As usual when I find a question on the internet describing my exact problem; there are no solutions! The only workaround I have noticed is that if you click on the containing div, then the editor, it works for a while, but as soon as you click any of the buttons it quickly fails again.

## Answer

**Svetoslav Dimitrov** answered on 10 Jun 2024

Hello Joshua, To achieve the desired behavior, set the EditMode of the Editor to Div. This is specific in the iframe, where it causes blur in the Incell of the Grid. Here is a REPL snippet where the Incell works with an editor in Div edit mode. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Lee** commented on 10 Jun 2024

Worked perfectly, thank you so much!
