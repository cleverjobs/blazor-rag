# AnimationContainer inside a Window is shown in the Background

## Question

**Hen** asked on 17 Jul 2024

How can I set the Z-index for the AnimationContainer to make it visible in the foreground ? I am using it inside a Window-Control (Modal=True) and that makes problems in my case...

### Response

**Hendrik** commented on 18 Jul 2024

.k-animation-container {
z-index: 99999;
} I figured it out.
