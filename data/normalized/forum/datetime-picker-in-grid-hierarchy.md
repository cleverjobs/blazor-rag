# DateTime picker in Grid Hierarchy

## Question

**Tac** asked on 10 May 2022

Hi all, I'm having a hard time implementing a DateTime picker in a Grid. I'd like to set up the grid using the hierarchy feature and implement InCell editing. I created a version of my problem in the Telerik REPL and have observed the same issue in my current code. [https://blazorrepl.telerik.com/wmEfuDcn54Cv6ZNO07](https://blazorrepl.telerik.com/wmEfuDcn54Cv6ZNO07) As you can see, the DateTime picker works fine in the parent table. But when it is implemented in the child table, it seems that clicking on the DateTime picker actually takes the cell out of focus. Does anyone know if there is a workaround or if this is a bug? Thanks Edit: I added the screenshots when I noticed that the REPL link wasn't loading correctly on my Chrome or Edge browser

## Answer

**Nadezhda Tacheva** answered on 12 May 2022

Hi Jon, As confirmed in your private ticket, this behavior is associated with a regression in the Grid. I am pasting the public bug report link here as well, so any other affected parties may follow its progress there: In hierarchical Grid with InCell edit trying to open the DatePicker or DateTimePicker popup of the child Grid closes the edited cell. Regards, Nadezhda Tacheva Progress Telerik

### Response

**TacoWombat** commented on 12 May 2022

Thanks for the follow up! For now, I think we'll use InCell editing in the parent rows and InLine editing in the Detail Template. Using InLine editing allows the datetimepicker to work as intended.
