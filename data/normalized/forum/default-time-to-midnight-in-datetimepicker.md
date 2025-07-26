# Default time to midnight in DateTimePicker.

## Question

**Mic** asked on 08 Apr 2022

Hi all, I am using the DateTimePicker with a nullable property public DateTime? EndDate { get; set; } When the user selects the picker, I would like the time defaulted to midnight as most times we use midnight, so it's a mission for users to always have to set the time to midnight when applying a date just a date. The time is there for the odd times we do want to have EndDate with a time - but's it is not the norm. Is there a way to tell the component to default to midnight?

## Answer

**Marin Bratanov** answered on 09 Apr 2022

Hi Michael, Is the goal that the users don't have to go through the Time portion of the DateTimePicker at all? If yes, perhaps you can simply use two separate components - a DatePicker and a TimePicker so that the users who don't want to touch time don't have to. The DatePicker sets the time to midnight by default. For a DateTimePicker, however, the goal is to let the user pick both at the same time. So, how would you expect that to default to midnight, since that would, effectively, take away the user's ability to pick time? Regards, Marin Bratanov Progress Telerik

### Response

**Michael** commented on 09 Apr 2022

Hi, Nope - if that was my goal I would use the DatePicker - yes? We are using the DateTimePicker because there may be times the user wants to also set the time - but mostly they just set date - so they have to keep altering the time to midnight. I did indicate this in my OP...

### Response

**Michael** commented on 09 Apr 2022

The time portion of the picker already defaults to a time - I just want to have the ability to control that default.

### Response

**Marin Bratanov** commented on 09 Apr 2022

Hello Michael, If you are in need of a fast response, I recommend opening a private support ticket, as they have a guaranteed response times. Forums do not have a guaranteed time, nor even a guaranteed response at all. As for reading and understanding your posts - I can assure you that I did. The thing is, such "defaulting" seems a little indeterministic until I can understand the goal. For example, what if there is already a value in the view-model? Should changing the date reset the time? Some users may want it, but others may not, how can the component know? Thus, how would you expect to be able to control that? Since, from the component point of view, this is heuristic, we default to the current time as that has been the most common request. That said, if you want to see a component behave in a different way than it does, you can also open an enhancement request in the Feedback portal (click the "Request a Feature" button at the top right), and explain the goal and requirements there - this will let the entire community see, evaluate and vote for this to support your idea, and our management review and prioritize it. I hope this information helps you streamline questions and requests you may have.

### Response

**Michael** commented on 09 Apr 2022

I am using a nullable variable as indicated in the opening post. If the value is NOT NULL, then the DateTimePicker reflects as much. This is not part of my question, and is pretty much unrelated. I want to control the initial state of the DateTimePicker when the NULLABLE variable is NULL - not when it has a value. If the value is NULL, the DateTimePicker is still showing a date and time when it initialises - and this is what I want control over. Maybe an event "OnInit"? The component currently initialises to the current time if no value provided. I want to control that time and default it to midnight instead of current time. Make sense now? In 9/10 cases, we just need the date, so midnight should be the default option as a convenience to the user so they don't have to always go to time and make it midnight (which is the current case). If however for the 1 in 10 times they do want a time, they have it right there to configure.

### Response

**Marin Bratanov** commented on 09 Apr 2022

Hi Michael, I would recommend you open an enhancement idea to explain how you want this to work. For example, should this be a new parameter or some event? If it is a parameter, when should it be used and how should its value be defined (for example, if you set it during initialization of the parent component it may no longer be the current time, which may still be wanted in some cases - while you want midnight, others may want something else). If it is an event, how should it be defined and work? Opening such a request is the best way to work towards adding such functionality in the product.
