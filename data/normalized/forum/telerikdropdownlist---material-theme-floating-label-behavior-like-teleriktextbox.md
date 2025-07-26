# TelerikDropDownList - material theme floating label behavior like TelerikTextBox?

## Question

**Bre** asked on 29 Jul 2020

This doesn't seem to be available by default? please advise on the usual... roadmap, places to upvote, temp workarounds, etc my initial rough workaround is some fairly manageable styling along these lines... <style> .k-dropdown { padding-top: 1.03125em; } .k-dropdown::after { content: "Gender"; color: rgba(0,0,0,0.6); position: absolute; margin-top: 0.5em; transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), color 0.4s cubic-bezier(0.25, 0.8, 0.25, 1); } .k-dropdown.k-state-focused::after, .k-dropdown:not(.k-state-empty)::after { transform: translate(-0.4em, -1.5em) scale(.75) ; } .k-dropdown.k-state-focused::after { color: #3f51b5; } </style>

## Answer

**Svetoslav Dimitrov** answered on 29 Jul 2020

Hello Brent, You can upvote and Follow the implementation of adding labels to all our components from this Feature Request on our public Feedback Portal. I have already given your Vote for it and you can Follow it for email notifications on status updates. Regards, Svetoslav Dimitrov
