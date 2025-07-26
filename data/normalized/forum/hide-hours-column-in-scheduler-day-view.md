# Hide Hours column in Scheduler Day View

## Question

**Emm** asked on 24 Nov 2021

Hi, I am trying to hide the hours column from the scheduler day view(please see screenshot) from what I can see, there is no property on the control to achieve this behavior. I would also like to stack the items on top of each other instead of horizontally.. Is there a way to achieve this? Thanks!

## Answer

**Emmanuel** answered on 25 Nov 2021

For anyone ending up here , here's how to hide the hours : <style> .k-scheduler-layout-flex .k-scheduler-cell.k-side-cell { display:none; } </style>
