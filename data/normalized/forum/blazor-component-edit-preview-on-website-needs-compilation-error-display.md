# Blazor component Edit/Preview on website needs compilation error display

## Question

**Ram** asked on 02 Sep 2022

Hello, the Edit/Preview box on the Blazor documentation is nice. Allows me to quickly try what the specific component or option does and allows. But, if I'm not mistaken, it does not display compilation errors anywhere and this makes the experience in case of an error really bad. For example, if I go to the Blazor MultiSelect page and edit the first editor available under the "Creating MultiSelect" header. If I make no mistakes, pressing the Preview button compiles the code cleanly and starts the Blazor component with my edits. But, if I make a mistake, let's say near the bottom of the Edit box I accidentally add an extra d to Add like so "Countries.Addd("Albania");", then after pressing the Preview button a couple of things might happen(?) If I had already successfully compiled some Blazor from your website, the Preview box will not update with the edits, but instead show the old compilation. and no errors anywhere. Can be very puzzling if the previous code was for.ex. from a different component alltogether If I didn't have an earlier compilation, kind of nothing happens. The Preview box display stays empty and there are no errors anywhere. So please add some kind of a popup with atleast an error saying "Hey, there's some problem with your code, we couldn't compile it, please take another look", or better yet, the actual error and line number if possible.

## Answer

**Dimo** answered on 02 Sep 2022

Hello Rami, Thanks for your feedback, we appreciate it. What you say makes sense and we considered such error reporting in the beginning. We concluded that there is not enough space for such interface. A more likely future solution will be to add easier transition from the docs snippet to the full-blown REPL app, which does display error messages. In the meantime, you can copy-paste the snippet manually. Regards, Dimo

### Response

**Rami** commented on 02 Sep 2022

Dear Dimo, thank you, the REPL app displays the errors nicely. I hope you are soon able to add links that open the code from the documentation to the REPL app. Regards, Rami
