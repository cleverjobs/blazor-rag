# Window immediately closes and then parent form OnValidSubmit() function is called

## Question

**Joh** asked on 04 Jun 2021

Hi there, I have a form: <TelerikForm Model="Template" OnValidSubmit="SubmitTemplateAsync"> <FormItems> <TelerikTextBox @bind-Value="Template.Title" PlaceHolder="Title"> </TelerikTextBox> <br /> @foreach (EvaluateQuestionGroup group in Template.QuestionGroups)
{ <TelerikTextBox @bind-Value="group.Title"> </TelerikTextBox> <TemplateLibraryEvaluateQuestionGrid Template="Template" QuestionGroup="group"> </TemplateLibraryEvaluateQuestionGrid> <br /> } </FormItems> </TelerikForm> The Grid in this form has a window component that allows a user to post comments about individual grid rows. To access this popup they click a telerikbutton rendered in a grid column which toggles the window and passes it the grid row as a Parameter. However, when a user clicks the button the window pops up and then immediately after OnInitializeAsync ends it disappears, at which point the form pasted above calls its OnValidSubmit. Can you tell me why this is happening? All the best, John

## Answer

**John** answered on 04 Jun 2021

So the solution was to move the event handler from a telerik button rendered in its own grid column to a gridcommandbutton rendered in the command column. Would still be interested to know why they work so differently.

### Response

**Svetoslav Dimitrov** answered on 09 Jun 2021

Hello John, Could you provide some more information on the setup of the Grid and the Models that you are using? From what I can see the Form is bound to a complex model. I am asking for more information so that we are able to properly investigate because the scenario you are facing seems like an odd one. The TelerikButton in a standard column should behave similarly to the GridCommandButton when we reference the OnClick event. The major difference is that the GridCommandButton provides an object of type GridCommandEventArgs, whereas the Button in a standard templated column would have access to the context. That being said, a runnable reproducible demo application would really help us to better determine and assist you in the situation you are facing. We genuinely love to help our fellow developers achieve beautiful and fully functional applications and this is our major priority. Regards, Svetoslav Dimitrov Progress Telerik
