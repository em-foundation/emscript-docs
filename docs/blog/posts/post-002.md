---
authors: [biosbob]
date: 2024-09-01
readtime: 5
---

# Announcing Zig&bull;EM v25.0.1

With support from **The EM Foundation**, we announce the initial release of **Zig&bull;EM** &ndash; a novel programming framework for developing and deploying applications which target resource-constrained MCUs, where every byte of memory and every &mu;Joule of energy matters.

<!-- more -->

<div markdown class="em-nav-arrow">

[&cularr;](/blog/post-001 "The EM language is dead, long live EM !!!")

{[sp,em-float-right][&curarr;](/blog/post-003 "Touring the Zig&bull;EM code-scape")}


</div>

<figure style="display:none" markdown id="fig0">
</figure>

## Setting expectations

As rationalized in our [previous](/post-001 "The EM language is dead, long live EM !!!") post, **Zig&bull;EM** strives to _reconstitute_&thinsp; core concepts and constructs of the [EM Programming Language](https://docs.openem.org/) into **Zig** &ndash; a system programming language favorably compared with Go and Rust, but with the simplicity and transparency of C. 

But downgrading the EM language into a programming framework hosted by Zig does introduce some challenges.&thinsp; For one, the Zig language itself remains a work-in-progress; reaching an "official" Zig 1.0 release will realistically require years of effort.(1)
{ .annotate }

1. see Andrew Kelley's [Zig 2024 Roadmap](https://lwn.net/Articles/959915/) talk

Furthermore, Zig eschews much of the "syntactic flexibility" (operator overloading, optional lexical elements, etc) found in contemporary languages ranging from C++ to Ruby &ndash; leaving us with a somewhat rudimentary set of programmatic mechanisms to realize **Zig&bull;EM**.

As a stand-alone language, EM could introduce keywords like <code class="language-zigem"><span class="k">config</span></code> and <code class="language-zigem"><span class="k">proxy</span></code> to reinforce its novel concepts; and EM's language translator could impart very specific meanings to otherwise stock programming constructs like <code class="language-zigem"><span class="k">module</span></code> and <code class="language-zigem"><span class="k">interface</span></code>.

Grafting EM onto Zig, however, requires us to operate within the syntactic and semantic constraints of the latter language.&thinsp; Ensuring that EM's concepts and constructs don't become "lost in translation", so to speak, emerges as our greatest challenge.

!!! info "FULL DISCLOSURE &ndash; My first impressions of Zig"

    Six months ago, I hadn't even _heard_&thinsp; of Zig&thinsp;!!&nbsp; In the interim, of course, I've not only immersed myself in the language but also managed to field my first iteration of the **Zig&bull;EM** framework.

    To understand my ever-growing fascination with Zig, let's roll the clock back to the 1980s &ndash; a time in which C had firmly established itself as a universal "middle-level" language &ndash; used for system programming on 8-bit microprocessors, 16-bit mini-computers, and 32-bit mainframes alike.

    Like Zig, the C language has no inherent runtime environment supported across all target processors.&thinsp; Building upon a "bare-metal" foundation, libraries of C functions (general-purpose or domain-specific) would address the runtime needs of a broad range of applications.
    
    Programmers generally characterize both C and Zig as inherently _small_&thinsp; languages &ndash; embodying a set of rudimentary mechanisms for constructing higher-level libraries, while staying close to the underlying hardware.&thinsp; As a consequence, C and Zig can remain maniacally focused on performance.(1)
    { .annotate }

    1. Andrew Kelley (the language's creator) refers <br> to Zig as _a DSL for emitting machine code._

    Pursuing an analogy, I've always viewed C as a "small town" &ndash; one whose streets and neighborhoods I've come to know like the back of my hand.&thinsp; By constrast, C++ has morphed into a "big city" &ndash; one with more streets than I could ever explore, and one with certain neighborhoods that the guide-books now tell me to avoid&thinsp;!!

    By maintaining a level of "small town" simplicity lacking in many modern compiled languages, Zig has emerged as a worthy alternative to C.&thinsp; This aspect of Zig also earns the language high-marks when compared against the complexity of Rust &ndash; another "big city" language that looks to supplant C++.  

    And finally, I can't say enough about the warm and welcoming Zig community I've joined at [Ziggit](https://ziggit.dev/) &ndash; where you really do feel that "small town" vibe.&nbsp; :sunglasses:

## Getting started

!!! tools "We've updated this material to reflect the latest release of **Zig&bull;EM**"

You can provision **Zig&bull;EM** v25.0.x on your host computer(1) in three simple steps:
{ .annotate }

1. presently &ndash; `windows-x86_64`, `linux-x86_64`, `macos-x86_64`

{[bx,1]} &nbsp; download/unpack [Zig v0.13.0](https://ziglang.org/download/), and add the {[sh]zig} command to your path<br>
{[bx,2]} &nbsp; download/unpack the latest **Zig&bull;EM** [sources](https://github.com/em-foundation/zigem-dev/releases), and {[sh]cd} into {[cf]zigem-dev/workspace} <br>
{[bx,3]} &nbsp; execute {[sh]zig build}, which will compile/install the **Zig&bull;EM** CLI program

When finished, verify your installation by executing {[sh]zig build verify}:

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][zigem-dev/workspace]}
$ {[sp,em-color-orange]zig build verify}
compiling META ...
    board: LP_EM_CC2340R5
    setup: ti.cc23xx://default
compiling TARG ...
    image sha: 57a5b811
    image size: text (1376) + const (364) + data (12) + bss (4)
done in 4.79 seconds</code></pre></div>

=== "Windows"

    <span class="em-small">You should install [Git for Windows](https://gitforwindows.org/), which includes the **Git Bash** shell as well as other stock CLI tools.</span>


<div id="zigem-command">
</div>
Going forward, we'll rely upon the {[sh]zig build zigem} sub-command to compile designated **Zig&bull;EM** programs targeting a particular MCU.&thinsp;  For example, the following command explicitly compiles our verification example:

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][zigem-dev/workspace]}
$ {[sp,em-color-orange]zig build zigem -- compile -f em.core/em.examples.basic/BlinkerP.em.zig}
compiling META ...
    board: LP_EM_CC2340R5
    setup: ti.cc23xx://default
compiling TARG ...
    image sha: 57a5b811
    image size: text (1376) + const (364) + data (12) + bss (4)
done in 4.67 seconds</code></pre></div>

!!! bulb "Consider creating a {[sh]zigem} command-line alias for the {[sh]zig build zigem --} prefix shown above"

## Exploring Zig&bull;EM

**Zig&bull;EM** supports just one target at this time &ndash; the Texas Instruments [CC2340R5](https://www.ti.com/product/CC2340R5) wireless MCU featuring a low-power Arm Cortex-M0+ CPU, a familiar suite of embedded peripherals, and a generic 2.4&thinsp;GHz radio with BLE 5.x support.(1)
{ .annotate }

1. While EM itself has supported dozens of 8/16/32-bit MCUs over the years, let's first focus on "getting **Zig&bull;EM** right" before we branch out to other hardware platforms.

We strongly encourage you to purchase an inexpensive [LP-EM-CC2340R5](https://www.ti.com/tool/LP-EM-CC2340R5) board from TI in their popular _LaunchPad_&thinsp; form-factor.&thinsp; In addition, you should obtain this [emulator board](https://www.ti.com/tool/LP-XDS110ET) if you don't already have TI-XDS110 support through another LaunchPad.

=== "MacOS"

    <span class="em-small">You'll also need to download [TI-UniFlash](https://dr-download.ti.com/software-development/software-programming-tool/MD-QeJBJLj8gq/8.7.0/uniflash_sl.8.7.0.4818.dmg) and install the application at its default location.</span>

Armed with target hardware, we can now compile _and_&thinsp; load our sample program by simply appending the {[sh]--load} ({[sh]-l}) option on our command-line:

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][zigem-dev/workspace]}
$ {[sp,em-color-orange]zigem compile -f em.core/em.examples.basic/BlinkerP.em.zig -l}
compiling META ...
    board: LP_EM_CC2340R5
    setup: ti.cc23xx://default
compiling TARG ...
    image sha: 57a5b811
    image size: text (1376) + const (364) + data (12) + bss (4)
done in 4.91 seconds
loading...
done.</code></pre></div>

!!! bulb "Use&thinsp; {[sh]zigem --help} followed by&thinsp; {[sh]zigem &lt;COMMAND&gt; --help} to learn more about the **Zig&bull;EM** CLI."

The {[cf]em.core/em.examples.basic} sub-folder contains over a dozen sample programs &ndash; each of which you can now compile and load onto your `LP-EM-CC2340R5` hardware.&thinsp;  While these programs do little more than blink LEDs, start immersing yourself in their overall structure:

```zigem linenums="1" title="em.examples.basic/BlinkerP.em.zig"
pub const em = @import("../../zigem/em.zig");
pub const em__U = em.module(@This(), .{});

pub const AppLed#t = em.import.@"em__distro/BoardC"#t.AppLed#t;
pub const Common#t = em.import.@"em.mcu/Common"#t;

pub const EM__TARG = struct {
    pub fn em__run() void {
        AppLed#t.on#f();
        for (0..10) |_| {
            Common#t.BusyWait#t.wait#f(500_000);
            AppLed#t.toggle#f();
        }
        AppLed#t.off#f();
    }
};
```

Our next few blog posts will deep-dive into this and other examples &ndash; focusing on core concepts and constructs first introduced in [EM](https://docs.openem.org/intro/)&thinsp;, but now seen through a Zig language lense.

!!! tip "Browsing the **Zig&bull;EM** sources using VS Code"

    The **VS Code - Zig Language** [extension](https://marketplace.visualstudio.com/items?itemName=ziglang.vscode-zig) goes a long way towards streamlining your exploration of **Zig&bull;EM** through features such as syntax highlighting and code navigation; a companion language server (**ZLS**) enables outline views, hover help, and intellisense completion.

    At the same time, the **Zig Language** extension knows nothing about the **Zig&bull;EM** framework per se; the extension renders {[cf]BlinkerP.em.zig} no differently from {[cf]build.zig} or any other Zig source file.

    We'll now released a fork of the Zig extension and language server which (through some minor modifications) has rudimentary awareness of **Zig&bull;EM**.&thinsp;  As illustrated by the example above, files like {[cf]BlinkerP.em.zig} would now have their EM-based constructs distinctly <span class="language-zigem"><span class="nb">highlighted</span></span> &ndash; further flattening your learning curve.

## Looking ahead

<div markdown class="em-ul em-ul-check">

skill-up on the Zig language, using Karl Sequin's [Learning Zig](https://www.openmymind.net/learning_zig/) as a starting-point

spend some cycles browsing the [zigem-dev](https://github.com/em-foundation/zigem-dev) snapshot downloaded earlier

direct all questions/comments to this [showcase post](https://ziggit.dev/t/introducing-zig-em/5794) on the **Ziggit** forum


</div>

{[hc]}
