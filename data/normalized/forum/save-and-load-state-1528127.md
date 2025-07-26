# Save and load state

## Question

**Mat** asked on 16 Jul 2021

Hello, if I serialize the grid-state and save it as a text-file, I get an incredible high table-width: 1772296985px - my workaround is to limit the tablke-width to max. 3000 px while saving and loading. The same with columns. Is there a bug? Thank you!

### Response

**Matthias** commented on 17 Jul 2021

Thank you for the quick response - obviously the template has changed. In newer applications, app { display: flex; } is no longer present. This also explains why the behavior did not occur in my test applications. Thank you very much for the hint. Unfortunately I can't remove app { display: flex; } as the layout would no longer be correct. But my workaround works quite well so far. So feel free to mark the question as answered.

### Response

**Marin Bratanov** commented on 17 Jul 2021

Glad to see you've solved this! I moved my comment to an answer and marked it. Thanks!

## Answer

**Marin Bratanov** answered on 17 Jul 2021

I recommend opening a ticket where you can send us a reproducible sample of this. You can use basic samples from our state docs to ensure it is runnable and does not depend on other pieces of the project. In the meantime, take a look at this article for a common reason that can cause the grid to actually have such a width: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-bootstrap-flex-width-issue](https://docs.telerik.com/blazor-ui/knowledge-base/grid-bootstrap-flex-width-issue)
