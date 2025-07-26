# TreeView checkboxes in Indeterminate state for last children

## Question

**Jac** asked on 25 Oct 2022

I have a case where I need to be able to set last children in indeterminate state. Yes, the indeterminate checkbox state for the node that has no children. Is it possible without any special hacks? I don't want to create my own checkboxes in templates, as I still need selecting parent. I'm already trying to do this with reflections and getting to ProcessedData (with some successes), but I'd prefer to use native functionality.

## Answer

**Dimo** answered on 27 Oct 2022

Hello Jacek, The indeterminate state can only be set by the TreeView itself, based on the state of child items' checkboxes. From this point of view, there is no built-in way to set indeterminate state manually. It seems that your scenario is even more special, as the desired checkboxes (items) have no children. So the possible options are templates or source code overrides. Regards, Dimo
