# Zig&bull;EM Programming Framework

Welcome to the world of **Zig&bull;EM** [_ˈzig.ɛm_&thinsp;] &ndash; a novel programming framework targeting resource-constrained embedded systems.&thinsp; To increase your understanding, this site documents all aspects of the **Zig&bull;EM** software platform.

<!-- imagemapper.noc.io -->

<div style="margin-bottom: -15px">
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1262 674">
  <image width="1262" height="674" xlink:href="/assets/splash.png"></image>
  <a xlink:href="https://www.linkedin.com/company/the-em-foundation/about/?viewAsMember=true" target="_blank">
    <rect x="6" y="500" fill="#fff" opacity="0" width="188" height="77"></rect>
  </a>
</svg>
</div>

!!! question "1 &mdash; Why another language"
    To fill a void...&thinsp; While **C** remains the dominant programming language for 8&thinsp;/&thinsp;16&thinsp;/&thinsp;32-bit microcontrollers [MCUs] with limited memory and processing resources, we see opportunites for a _higher-level_ language which at the same time paves the way for _higher-levels_ of embedded system performance.

!!! question "2 &mdash; Where does EM make its greatest impact"
    Quite simply, by reducing overall program size &ndash; a careabout for software developers working with resource-constrained MCUs.&thinsp; Reducing runtime memory requirements not only can improve program execution time, but can dramatically lower overall power consumption within the MCU as well.

    Though the EM language translator ultimately generates (portable) C/C++ code as output, a novel _configuration_ phase within the program build-flow serves as the "secret sauce" behind these performance improvements.

    A quick pass through&thinsp; [EM&thinsp;.&thinsp;optimize = WPO&thinsp;+&thinsp;ACO](//blog.openem.org/post-005/){ .em-link } &thinsp;should offer some more insights.



