# ComboBox with same text field always selects first one

## Question

**Chr** asked on 03 Mar 2021

I have the following ComboBox with some bad data (fixing the data is on the list to do, but the system will launch with bad data.) AllContacts is pulled from <TelerikComboBox Data="AllContacts" TextField="FullName" ValueField="Id" TValue="int?" TItem="TblCompanyContact" Width="100%" Value="ContactId" ValueChanged="@( (int? c)=> ChangeDropDownContact(c) )" Filterable="true" FilterOperator="StringFilterOperator.Contains"> </TelerikComboBox> @code{ List<TblCompanyContact> AllContacts; int? ContactId; protected void ChangeDropDownContact(int? c) { if (c !=0 && c !=null) { //more code will go here when c is not null ContactId=c; } else { ContactId=null; } }

## Answer

**Chris** answered on 03 Mar 2021

Sorry, posted before I was ready. AllContacts is loaded on iniitalize and has data like this ID=1, FullName="John Smith" ID=2, FullName="John Smith" ID=3, FullName="John Smith" ID=4, FullName="Alice Jones" ID=5, FullName="Michael Jones" If I select John Smith with ID of 2 or 3 and then the focus is lost, the ChangeDropDownContact fires again but it always returns the first ID that matches the name, in that case 1. If I choose ID of 5 and focus is lost, it the change fires again and picks ID of 4. Any idea what I might be doing wrong?

### Response

**Chris** answered on 03 Mar 2021

I really wish there was an edit button for posts, i keep messing up! ID 5 should be Alice Jones again. It only happens when the name is exactly the same.

### Response

**Svetoslav Dimitrov** answered on 04 Mar 2021

Hello Chris, Thank you for bringing this to our attention. As a small token of appreciation, I have updated the Telerik Points for your account. That being said, I have logged a new Bug Report on your behalf on our public Feedback Portal. I have given your Vote for it and since I added it from your account you are automatically subscribed to receive email notifications on status updates. Regards, Svetoslav Dimitrov
