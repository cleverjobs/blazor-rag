# Form with TabStrip: invalid inputs NOT highlighted in unvisited tabs

## Question

**Boh** asked on 09 Jun 2025

Hi, I'm currently using a TelerikForm with built-in validation and TelerikTabStrip to split the form into multiple tabs. I’m using a single shared EditContext for the entire form, covering fields across all tabs. The issue I'm facing: When I trigger form validation (e.g. by clicking Submit), only the fields in the currently visible tab get proper validation UI (.k-invalid, red borders, etc.). Fields in tabs not yet visited do not show red borders around input fields — only the validation summary displays the error messages (and labels are red for those fields which is ok). You can observe this issue directly in your own official demos: Demo Once I manually visit each tab, the fields inside do react to validation as expected (input fields appear with red borders). But still - all of it works only with PersistTabContent parameter set to true (meaning behaviour when user visits some tabs, clicks submit elsewhere and gets back to tabs already visited.) without PersistTabContent checked - it doesn't work at all. This behavior leads to a confusing and inconsistent UX, especially in forms that do not have visible labels next to each field — users don’t realize what’s wrong until they manually visit every tab. My questions: -Is there any workaround to make validation styles apply to inputs in all tabs, even those not yet rendered without need to manually render all the tabs content? -Is there a planned feature or improvement to address this? If not, I’d like to formally request this as must-have functionality. As it stands now, this issue severely degrades the user experience. Validation messages show in the summary, but without any visual feedback in the inputs — especially in unvisited tabs — users are left confused. In practical terms, tabs become unusable for serious forms when this happens. If users have to manually check every tab just to find the highlighted fields, it defeats the purpose of having tabs in the first place. Thanks for any help! -Bohdan

## Answer

**Hristian Stefanov** answered on 11 Jun 2025

Hi Bohdan, Let me shed some light on the scenario here. I see two practices being used that aren't ideal. The first is marking form fields as invalid on initial load, and the second is validating fields that haven't been rendered yet. Both are generally considered bad practices — showing users invalid fields right when a form or a form section opens is not user-friendly and goes against good design principles. I’m aware that our demo does show validation for fields that aren’t yet rendered. However, the only reason that demo exists is because many customers, despite it being a poor approach, use forms this way inside tabs. That said, if you still want to validate hidden fields as soon as they're rendered, you can call the Validate() method during the TabStripActiveTabIndexChanged event. Here’s something you can start with: <TelerikTabStrip ActiveTabIndex="@TabStripActiveTabIndex" ActiveTabIndexChanged="@TabStripActiveTabIndexChanged" /> @code {
private EditContext? JobEditContext { get; set; }

private int TabStripActiveTabIndex { get; set; }
private bool ShouldRevalidateForm { get; set; }

private void TabStripActiveTabIndexChanged(int newIndex)
{
TabStripActiveTabIndex=newIndex;

if (JobEditContext?.GetValidationMessages().Count()> 0)
{ ShouldRevalidateForm=true; }
}

protected override async Task OnAfterRenderAsync(bool firstRender)
{
if (ShouldRevalidateForm)
{
ShouldRevalidateForm=false; JobEditContext?.Validate(); StateHasChanged();
}

await base.OnAfterRenderAsync(firstRender);
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Michał** commented on 11 Jun 2025

Your documentation provides a solution, yet your response suggests that this approach is suboptimal and should not be used. If this is the case, the documentation should clearly state, "This is a poor approach. We implemented it, but it is not recommended for use." We believe that if a solution is documented, it should be functional. We understand that without using "PersistTabContent," the feature will not work. However, when "PersistTabContent" is used, it should operate correctly. As my colleague mentioned, once each tab is visited and all items appear in the DOM, everything works fine. If there were an option, in addition to "PersistTabContent," to force render all groups/tabs at once (all DOM representation created at the beginning), we would achieve our goal. We aim to display our groups as either groups or tabs, with all validation features working regardless of the chosen approach. Please consider our requirement. Best regards.

### Response

**Hristian Stefanov** commented on 12 Jun 2025

Hi Michał, Rest assured, we will enhance the demo and update the description to clarify that the example does not represent UX best practices. However, it is still a commonly used approach among developers. As for your requirement, the guidance I shared in my previous message appears to address what you're looking for. Kind Regards, Hristian
