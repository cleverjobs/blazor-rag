# Force Refresh TelerikEditor

## Question

**Lou** asked on 29 Apr 2022

Hi, I am looking for a way to force TelerikEditor to be updated when the parent component change states without using 2 ways binding. <TelerikEditor @ref="Editor" DebounceDelay="300" Value="@DefaultValue" EditMode="@EditorEditMode.Div" Height="650px" Width="1400px">
</TelerikEditor>

@code { private string? DefaultValue { get; set;} public TelerikEditor Editor { get; set; }=null!;

} Currently, the value of the of Telerik Editor is bind with DefaultValue. Is there away to force Editor Value to refresh as soon as DefaultValue changes without using 2 ways binding?

### Response

**Nadezhda Tacheva** commented on 03 May 2022

Hi Louis, I see that a private thread has already been submitted on the matter. It is currently under revision. Once the case is resolved, we will post an update here to share the suggested approach with the community.
