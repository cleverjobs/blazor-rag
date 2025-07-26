# Using the same format for read-only display and editing

## Question

**Joh** asked on 27 Jun 2021

I have a grid. I am using a custom form to display details and edit the details. I am using this ... <LienholderDetails @bind-SelectedRecord="@selectedRecord" mode="@mode" OnSave="@Save" OnClear="@ClearSelection"> </LienholderDetails> in the parent component after the grid. @mode is add, view, edit, etc. And I use textboxes in the child component ... <TelerikTextBox @bind-Value="@SelectedRecord.Name" Label="Company Name" Enabled="@enabled" /> which are enabled or not depending on the mode passed as a parameter. If a user is authorized to edit the details and clicks "Edit" I wanted to either call the child component with enabled=true or set the @enabled value to true in code. This avoids having two identical layouts, one enabled and one not. How would I go about this? Obviously I would do this for other control types as well.

## Answer

**John** answered on 27 Jun 2021

I did some experimenting, then backed up a step. Then the answer became obvious. My Detail component is initialized and is a PART of my parent form, just invisible until the user clicks a button to initialize a copy of the record for editing. From the sample. So by changing this <LienholderDetails @bind-SelectedRecord="@selectedRecord" mode="@mode" OnSave="@Save" OnClear="@ClearSelection"> </LienholderDetails> to this <LienholderDetails @bind-SelectedRecord="@selectedRecord" mode="@mode" enabled="@enabled" OnSave="@Save" OnClear="@ClearSelection"> </LienholderDetails> with the @enabled being set to true or false in the parent form depending on the button clicked, StateHasChanged will refresh the data entry fields to enabled or not.

### Response

**John** commented on 27 Jun 2021

Now I only need one "detail" form per entity and one "grid" form per entity.
