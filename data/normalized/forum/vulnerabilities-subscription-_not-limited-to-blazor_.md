# vulnerabilities subscription (not limited to blazor)

## Question

**Ale** asked on 07 Mar 2021

Hello All, found that from time to time there are some vulnerabilities found in some products ([https://www.telerik.com/support/kb/aspnet-ajax/details/cryptographic-weakness),](https://www.telerik.com/support/kb/aspnet-ajax/details/cryptographic-weakness),) luckily we do not use asp.net ajax, but is it possible to have email subscription to be noticed as soon as any found? Thx Alex

## Answer

**Dimo** answered on 08 Mar 2021

Hello Aleksandr, We send mass emails about reported major vulnerabilities to all license holders and assigned developers, for both active and expired licenses. Subscription options for all reported vulnerabilities exist via third-party services which we use: Create a custom RSS feed on one of the prominent websites where we disclose reported security vulnerabilities: [https://www.cvedetails.com/vulnerability-feeds-form.php](https://www.cvedetails.com/vulnerability-feeds-form.php) [https://www.cvedetails.com/vendor/14130/Telerik.html](https://www.cvedetails.com/vendor/14130/Telerik.html) Subscribe to the RSS feed for the product's release notes. Please note it may not be obvious that a given fix is related to security. We use this approach on purpose. (RSS) [https://www.telerik.com/feeds/ui-for-blazor-whats-new](https://www.telerik.com/feeds/ui-for-blazor-whats-new) (web page) [https://www.telerik.com/support/whats-new/blazor-ui/release-history](https://www.telerik.com/support/whats-new/blazor-ui/release-history) We also log reported security vulnerabilities at cve.mitre.org. Regards, Dimo
