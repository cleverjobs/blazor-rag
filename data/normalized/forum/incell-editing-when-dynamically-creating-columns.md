# Incell editing when dynamically creating columns

## Question

**Joh** asked on 26 May 2021

Hi there, I've created a grid with columns that can be added dynamically, but I'm unable to use incell editing in the dynamically created columns. QuestionData is a Dictionary<string, object> Source below: <TelerikGrid Data=@QuestionGroup ScrollMode="@GridScrollMode.Scrollable" Height="35vh" EditMode="@GridEditMode.Incell" Resizable="true" @ref="gridref" Reorderable="true" RowDraggable="true" OnRowDrop="@((GridRowDropEventArgs<EvaluateQuestion> args)=> OnRowDropHandler(args))" OnCreate="@CreateHandlerAsync"> <GridSettings> <GridRowDraggableSettings DragClueField="@nameof(EvaluateQuestion.Title)"> </GridRowDraggableSettings> </GridSettings> <GridToolBar> <GridCommandButton Command="Add"> New Question </GridCommandButton> <TelerikButton OnClick="NewColumn"> New Column </TelerikButton> <TelerikButton OnClick="RemoveGrid"> Remove Grid </TelerikButton> </GridToolBar> <GridColumns> <GridColumn Field="Title"> </GridColumn> <GridColumn Field="FullQuestion"> </GridColumn> @foreach (string entry in Template.ColumnHeadings)
{ <GridColumn Title="@entry"> <Template> @{
var c=context as EvaluateQuestion;
if (c.QuestionData.TryGetValue(entry, out var check))
{
@c.QuestionData.Where(v=> v.Key==entry).FirstOrDefault().Value
}
else
{
c.QuestionData.Add(entry, new string("test"));
}
} </Template> <EditorTemplate> </EditorTemplate> </GridColumn> } </GridColumns> </TelerikGrid> public void NewColumn ( ) {
Template.ColumnHeadings.Add( new string ( "Placeholder" ));
StateHasChanged();
}

## Answer

**Hristian Stefanov** answered on 26 May 2021

Hi John, If you are using version 2.23.0, there was an issue where Grid bound to ExpandoObject throws an error with InCell editing. In the latest version (at the moment of writing 2.24.0), the issue is fixed. Make sure you have updated to our latest version. In the attached example project, I have prepared for you an approach of how to use InCell Editing on the dynamically created columns. The project showcases how to achieve the desired result, using the OnUpdate event with the UpdateHandler method and InCell EditMode on the Grid. You could try to compare both projects and see where something is missing. In the attached incell-editing-behavior.gif file, you can see the result from the example project. I hope this helps and if you have any other questions or I'm missing something from the scenario, please let me know. Regards, Hristian Stefanov Progress Telerik
