# Proper way to reflect changes to a child control when a Combo box in parent is changed?

## Question

**Joh** asked on 19 Feb 2025

I have a child component that I am trying to get to re-render when a new value on a combo box on the parent component is changed. My child control is not re-rendering to reflect the value change. This is my current code: <TelerikComboBox @bind-Value="@SelectedId" FilterOperator="@filterOperator" Data="@ParticipantsDDL" TextField="@nameof(ParticipantDDL.CodeName)" ValueField="@nameof(ParticipantDDL.Id)" Placeholder="Select/enter a participant code or name." Width="40vh" DebounceDelay="200" OnChange="@OnComboValueChanged" Filterable="true"> </TelerikComboBox> @if (SelectedId> 0)
{ <PDParticipant ParticipantId="@SelectedId" /> } And my Handler: private void OnComboValueChanged ( object newValue ) {
SelectedId=( int )newValue;
StateHasChanged();
} When I select a new value in the Combo box the SelectedId value changes on the parent page but I need to force the child control to re-render with the new code. How do I force the child control to rerender with the new data?

### Response

**Dimo** commented on 21 Feb 2025

@John - the provided work works, so the problem is most likely somewhere else.

### Response

**Anislav** commented on 27 Feb 2025

Are there any specific details, such as the parent and child components being placed in a dialog?

### Response

**Dimo** commented on 27 Feb 2025

Yes, see Dialog Reference and Methods The Dialog is rendered as a child of the TelerikRootComponent, instead of where it is declared. As a result, it doesn't automatically refresh when its content is updated. In such cases, the Refresh method comes in handy to ensure that the Dialog content is up-to-date.
