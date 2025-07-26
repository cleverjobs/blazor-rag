# Unpredictable Tooltip Behavior

## Question

**Iva** asked on 22 Oct 2022

1. Go to [https://demos.telerik.com/blazor-ui/gantt/templates](https://demos.telerik.com/blazor-ui/gantt/templates) 2. Scroll to the end of timeline horizontally 3. Move mouse pointer to timeline Tooltip appears in the wrong place t

### Response

**Hristian Stefanov** commented on 26 Oct 2022

Hi Ivan, Thank you for giving such clear steps to reproduce the behavior. Indeed, the tooltip tries to show in the middle of the task, but when part of the task is hidden, the tooltip appears in strange places. I will discuss the situation with our development team, and I will get back to you with more details shortly here.===ADMIN EDIT===As a result of further investigations and discussions, it turned out that this is an actual bug in the Gantt. Here is the public item for it: Timelines that are longer than the viewport make their tooltips mispositioned. Thank you for reporting. Kind regards, Hristian
