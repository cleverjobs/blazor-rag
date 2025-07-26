# Notification Only Works from Some Code

## Question

**Ada** asked on 30 Jun 2022

This turned out to be a cache problem. Thought I cleared it, but apparently not. Today it works. I'm trying to implement some very basic toast notifications in a simple form WASM app. There are two code paths where notifications would be displayed, based on form data. One of them works perfectly every time. The other refuses to work at all, despite the code being called. I've tried all of the usual Visual Studio things (clean, deleting bin/obj, restarting, etc.) and the behavior persists. There's nothing in the browser's console to indicate a failure. This is my first attempt at using a Telerik control. It's also my first real Blazor app. Maybe there's something basic I didn't do correctly that's causing weird side effects. Nothing else really makes sense considering how simple this code is. Here's the UI bits... <TelerikNotification @ref="@NotificationReference" Class="MyTelerikNotification" VerticalPosition=NotificationVerticalPosition.Top HorizontalPosition=NotificationHorizontalPosition.Center> </TelerikNotification> <h3> @FlightTitle </h3> <ul> @foreach (var question in ThisFlightForm.Form.TrueFalseQuestions)
{ <FormQuestionTrueFalse thisFormItem=question /> } </ul> <div> <button @onclick="OnClick_BtnSubmit" class="btn"> Submit </button> <button @onclick="OnClick_BtnCancel" class="btn"> Cancel </button> </div> Inside the code block is the Notification Reference declaration: public TelerikNotification NotificationReference { get; set; }=new (); Here's the method call that's having issues. The obvious thing to check is the value of canSubmit, which works perfectly fine. If I put the ShowToasts calls from the IF down into the ELSE, they are fine. private void OnClick_BtnSubmit ( ) { var canSubmit=_preSubChecks.CanFormBeSubmitted(ThisFlightForm); if (canSubmit.ChecksPassed)
{ //this does not work at all, despite being called ShowToasts( $"Unable to submit form - {canSubmit.ErrorMsg} ", ThemeConstants.Notification.ThemeColor.Error);
ShowToasts( "Submitting Form", ThemeConstants.Notification.ThemeColor.Info);
ShowToasts( "Success!", ThemeConstants.Notification.ThemeColor.Success);
} else { //this works fine ShowToasts( $"Unable to submit form - {canSubmit.ErrorMsg} ", ThemeConstants.Notification.ThemeColor.Error);
}

} Here's the method that shows the toast notifications. I added a temp var and a console out so I could verify the object wasn't null for some reason. private void ShowToasts ( string msg, string toastType ) { var tmpNm=new NotificationModel()
{
Text=msg,
ThemeColor=toastType,
};
NotificationReference.Show(tmpNm);
Console.WriteLine(JsonConvert.SerializeObject(tmpNm));
} Here's the output from the console logs where the Notification control refuses to display (the if): {"ThemeColor":"error","Closable":true,"CloseAfter":5000,"ShowIcon":true,"Icon":null,"Text":"Unable to submit form - "}
{"ThemeColor":"info","Closable":true,"CloseAfter":5000,"ShowIcon":true,"Icon":null,"Text":"Submitting Form"}
{"ThemeColor":"success","Closable":true,"CloseAfter":5000,"ShowIcon":true,"Icon":null,"Text":"Success!"} The first Notification (the error) is only here just to make sure the problem wasn't the content or the Notification display type being a problem. Here's the output from the one that works (the else): {"ThemeColor":"error","Closable":true,"CloseAfter":5000,"ShowIcon":true,"Icon":null,"Text":"Unable to submit form - At least one question was not answered"} Aside from the Text, this is exactly the same as the error notification I put into the code that refuses to work.

## Answer

**Adam** answered on 01 Jul 2022

This turned out to be a cache problem. Thought I cleared it, but apparently not. Today it works.
