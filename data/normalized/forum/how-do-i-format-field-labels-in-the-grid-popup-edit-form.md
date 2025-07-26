# How do I format field labels in the grid popup edit form?

## Question

**Joh** asked on 29 Aug 2024

How do I format field labels in the grid popup edit form? I want to style the labels on a popup edit form. I also would like to associate the labels with fields. <GridColumn Field="@nameof(ParticipantVM.ParticipantCode)" Width="100px" Filterable=true> <EditorTemplate> @{
var item=(ParticipantVM)context; <div @onkeydown:stopPropagation> <TelerikTextBox @bind-Value="@item.ParticipantCode" Id="pcode" Placeholder="Enter a Code" DebounceDelay="0" /> </div> } </EditorTemplate> </GridColumn>

## Answer

**Dimo** answered on 30 Aug 2024

Hello John, The Grid uses the column Title as a field label in the Grid popup edit form. If the column Title is not set, then the Grid uses the column Field. If you need additional customization and the column Title is not enough for you, then you may need to use a full Grid popup form template. Regards, Dimo
