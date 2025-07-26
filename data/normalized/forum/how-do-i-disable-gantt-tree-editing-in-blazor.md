# How do I Disable Gantt Tree editing in Blazor?

## Question

**AshAsh** asked on 17 Feb 2022

I want to disable Gantt tree editing. ie make the tree read only. Any suggestions?

## Answer

**Benjamin** answered on 21 Feb 2022

Hey Ash, we have to wait until R2 2022 (early march) will come out - then you can hook into the OnEdit - until that: You can't toggle the state.

### Response

**Apostolos** answered on 21 Feb 2022

Hello Ash, We will introduce new editing modes for the Gantt in our 3.1 version release which is due in early March. It will be possible to set the edit mode of the Gantt TreeList to none, thus, disable editing. Additionally, we will add new events including the OnEdit event for Gantt. The OnEdit event will give developers the ability to cancel edit based on a condition. I hope you find the above information useful and the release date fits your time frame. Regards, Apostolos

### Response

**Benjamin** answered on 02 Mar 2022

Hey Ash, as you might seen in the news, Editable is possible now :) You can add the "Editable" for each Column now. Happy coding!

### Response

**Debra** commented on 13 Jul 2022

Yes. But doesn't that only disable editing on the columns? What about making the tree (is that what the part on the right is called) read-only? If someone double-clicks on a dark line, I don't want the Task pop-up to even show. Can I disable that?

### Response

**Dimo** commented on 18 Jul 2022

@Debra - see Disable editing or dragging of tasks on timeline (Timeline read-only mode) I also voted on your behalf for the relevant feature request.
