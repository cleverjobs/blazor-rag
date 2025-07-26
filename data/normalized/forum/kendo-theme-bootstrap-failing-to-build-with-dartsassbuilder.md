# Kendo-Theme-Bootstrap failing to build with DartSassBuilder

## Question

**Ben** asked on 01 Oct 2024

Hi, We're trying to make use of Telerik's NPM package with our Blazor project, along with that we want to only implement the individual components we want to use for our stylesheet instead of using `dist/all. We are using DartSassBuilder to compile our SCSS files. Below are screenshots of our implementation: With this we are unable to actually build the app, the build errors didn't work well, but even changing this to use WebCompiler it doesn't work: It seems both DartSassBuilder and WebCompiler can't make use of the @naming, and we're unsure of what to do to solve this. Note: - Everything will work if we just run it with `dist/all.scss`, however to make the app load faster we want to rather compiler our own custom SCSS solution, namely for Grid and some inputs. - This is the second blazor project with this issue. - Both projects use Blazor WASM Standalone

### Response

**Craig** commented on 01 Oct 2024

We found WebCompiler is a bit outdated for SASS, won't support newer SASS features. Our dev ops wound up using sass-loader

### Response

**Vessy** commented on 02 Oct 2024

Thanks a lot for the update and sharing the found solution with the community, Craig. I am glad to hear that everything is working properly at your end now.

### Response

**Benjamin** commented on 02 Oct 2024

Hi @Vessy There is no found solution, this is a help request. I still need to test sass-loader, however we would like a more drop and play from a more NPM solution, such as using DartSassBuilder

### Response

**Vessy** commented on 07 Oct 2024

Hi, Benjamin, Apologies for the misunderstanding. In such case, can you try the configurations shared by my colleague epetrow in the following github post and see whether this will solve the issue at your end as well? [https://github.com/telerik/kendo-themes/issues/5090#issuecomment-2232934996](https://github.com/telerik/kendo-themes/issues/5090#issuecomment-2232934996) Just make sure that you replace the "provider" value with the one actually used in your end (e.g with "unpkg" i the themes are taken from there).
