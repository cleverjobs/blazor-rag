# NullReference Exception when Filter applied

## Question

**Coo** asked on 21 Sep 2022

I have a TelerikGrid that I set the filter state using the OnStateInit method. This work fine and the menu item shows up blue to indicate that it is in use, but when I choose that column menu and the Filter option an unhandled exception occurs. I have produced a demo and been able to reproduce the issue, located here - [https://blazorrepl.telerik.com/wcYDwFbw26v6wIqr52](https://blazorrepl.telerik.com/wcYDwFbw26v6wIqr52) I'm guessing that there is some setup missing, but from reading the documentation, I can't seem to find it.

## Answer

**Coops** answered on 21 Sep 2022

My team found the solution, I had used the constructor that takes three arguments. In fact an object initialiser is needed that set the 'MemberType' property also. So instead of: new FilterDescriptor( "Flow.FlowType", FilterOperator.Contains, FlowType) I needed to use: new FilterDescriptor
{
Member="Flow.FlowType",
Operator=FilterOperator.Contains,
Value=FlowType,
MemberType=typeof ( string )
}

### Response

**supachris28** answered on 21 Sep 2022

The MemberType of the FilterDescriptor needs to be set. The constructor really should be updated to include this.
