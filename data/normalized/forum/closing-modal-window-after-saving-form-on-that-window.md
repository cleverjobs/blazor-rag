# Closing Modal Window after saving form on that window?

## Question

**Jst** asked on 23 Mar 2023

I have a Windows setup as a modal. On the window I have a small form. When I hit the save button on the form the data saves but then I want to automatically close the modal window. This is my Save method: private bool isModalVisible { get; set; }=false; protected void OnDoubleRowClickHandler ( GridRowClickEventArgs args ) {
isModalVisible=true;
} public async void OnSubmitHandler ( EditContext editContext ) { bool isFormValid=editContext.Validate();
MyVM myClass=(MyVM)editContext.Model; if (isFormValid)
{ var result=await _myService.SaveMyClass(myClass);
isModalVisible=false;
}
} I make the modal window visible in a double-click event on a grid row. HYow do I close the modal from inside my SubmitHandler method?

### Response

**Hristian Stefanov** commented on 28 Mar 2023

Hi John, I carefully reviewed the provided Save method, and it looks OK. I copied it and recreated the described scenario (excluding Grid) in this REPL link. It seems that changing the i sModalVisible to false closes the window modal successfully. Please run and test the REPL to see if the result you get is the same. Use the above sample as a comparison. If there is still a problem with closing the window in the submit handler, modify the REPL to reproduce it and send it back to me. That will allow me to see the behavior firsthand and suggest next steps. I look forward to hearing your feedback. Kind Regards, Hristian
