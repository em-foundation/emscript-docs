---
authors: [biosbob]
date: 2024-09-15
readtime: 10
---

# Touring the Zig&bull;EM code-scape

The next few blog posts will explore the **Zig&bull;EM** programming framework in ever-greater detail &ndash; starting with instructions for installing the latest software version, and then moving on to a 10,000' overview that touches upon some core concepts and constructs of **Zig&bull;EM**.

<!-- more -->

<div markdown class="em-nav-arrow">

[&cularr;](/blog/post-002 "Announcing Zig&bull;EM v25.0.1")

</div>

## Updating your installation

The process for (initially) installing and (subsequently) updating your local version of **Zig&bull;EM** boils down to three basic steps:

<div markdown class="em-ul em-ul-bull">

</div>

{[bx,1]} &nbsp; install [Zig](https://ziglang.org/download/)<br>
{[bx,2]} &nbsp; clone [zigem-dev](https://github.com/em-foundation/zigem-dev/)<br>
{[bx,3]} &nbsp; execute {[sh]zig build}

As part of step {[bx,1]}, you should have added the `zig` executable to your path.&thinsp; Invoke the {[sh]zig version} command for confirmation.(1)
{ .annotate }

1. **Zig&bull;EM** currently requires version 0.13.0 of Zig

As for step {[bx,2]}, an initial {[sh]git clone} and subsequent {[sh]git pull} of the {[cf]zigem-dev} repository will take you to the latest release of **Zig&bull;EM**.&thinsp; Tags on the main branch (`v25.0.1`, `v25.0.2`, ...) enable you to easily move to earlier releases.(1)
{ .annotate }

1. If you wish to avoid the {[sh]git} command altogether, just<br>download the sources for individual [releases](https://github.com/em-foundation/zig-em-dev/releases).

Step {[bx,3]} will then build the {[sh]zigem} command-line executable, as well as download/install other required artifacts.&thinsp; Invoke {[sh]zig build verify} as a final test.

!!! info "You may want to consult these [Getting started](/post-002/#getting-started) instructions for more detail on first-time installation."

!!! zig "The Zig cache &mdash; a cornerstone of {[sh]zig build}"

    As you might expect, the first invocation of {[sh]zig build} can take a fair amount of time; subsequent invocations of {[sh]zig build}, however, can complete almost instantenously.&thinsp;  Not unlike `make`, the zig build-system strives to perform the minimal number of steps required to complete the task at hand.

    Should you choose to learn more(1)about the build-system, you'll quickly come to appreciate the critical role played by the **Zig cache** &ndash; a fascinating foundational element first described [here](https://ziglang.org/download/0.4.0/release-notes.html#Build-Artifact-Caching) in detail.&thinsp;  In simple terms, virtually any artifact touched when invoking {[sh]zig build} will persist in Zig's filesystem cache.
    { .annotate }

    1. [ziglang.org](https://ziglang.org/learn/build-system/ "standard documentation")<br>[zig.news](https://zig.news/xq/zig-build-explained-part-1-59lf "introductory tutorial")<br>[kristoff.it](https://kristoff.it/blog/maintain-it-with-zig/ "building C/C++")<br>[michelh.com](https://mitchellh.com/zig/build-internals "build-system internals")

    Strange as it may seem, you won't find anything resembling a {[sh]zig clean} command; all cached artifacts have a unique content-based identifier.&thinsp;  But sometimes to alleviate any lingering doubts about cache coherence, I will delete the special `.zig-cache/` and `zig-out/` folders in the repository's root before invoking {[sh]zig build}. :wink:

The artifacts provisioned through {[sh]zig build} include a version of this [Zig Language](https://marketplace.visualstudio.com/items?itemName=ziglang.vscode-zig) extension for **VS Code** &ndash; specially modified to add awarenesss of the **Zig&bull;EM** framework.&thinsp; Forked from upstream repositories, this extension currently functions as a "drop-in" replacement.(1)
{ .annotate }

1. If you've already installed the stock **Zig Language** extension,<br>you'll have to disable it within the `zigem-dev` workspace.

To install, invoke **Extensions: Install from VSIX...** from the VS Code **Command Palette** and then navigate to your `zigem-dev/zig-out/tools/` folder.&thinsp; This folder should contain a file named <code>vscode-zigem-*VERSION*.vsix</code>, which you can now select and **Install**.(1)
{ .annotate }

1. If you find multiple `.vsix` files in the folder, select the one with the highest <code>*VERSION*</code> number.

Once complete, invoke **Command Palette > Developer: Reload Window** to refresh your workspace.&thinsp; If all goes as planned, you'll see a **Zig&bull;EM activated** popup appear briefly.

## Repository organization

With our `vscode-zigem` extension in place, let's start exploring the `zigem-dev` repository itself &ndash; beginning with its top-level organization as a "typical" Zig project:

<figure markdown id="fig1">
![Image info](/assets/fig-003-1.png)
<figcaption>Zig Project 
</figure>

!!! zig "It all starts with `build.zig`"

    Even if you never plan to follow-up on the {[sh]zig build} references cited earlier, do invest under a minute of your valuable time digesting this material found at [zig.guide](https://zig.guide/build-system/zig-build).

Drilling down into the special `workspace/` folder highlighted above, we formally enter the domain of **Zig&bull;EM** &ndash; featuring a number of **packages** with (unique) names like {[ze,kt]em.core}, which in turn contain (uniquely-named) **buckets** such as {[ze,kt]em.utils} and {[ze,kt]em.examples.basic}.

<!--
!!! info "When mature, this embryonic `workspace` folder will cleave from the main **Zig&bull;EM** repository."
-->

<figure markdown id="fig2">
![Image info](/assets/fig-003-2.png)
<figcaption>Zig&bull;EM Workspace 
</figure>

A **Zig&bull;EM** workspace contains a special `zigem.ini` file at its root, along with a distinguished `zigem-package.ini` file at the top of each **package** found therein.&thinsp; We'll visit these as well as other `.ini` configuration files over the course of time.

<!--
!!! abstract "Terminology&thinsp;:: **Zig&bull;EM** = Zig + EM"

    Mapping core concepts and constructs of the original [EM language](https://docs.openem.org/) into Zig will invariably lead to _terminology clashes_, in which a term like **package** has a distinct meaning in each language domain.&thinsp; When ambiguities do arise, we'll qualify these terms in context.
-->

Descending one more level in our **package &gt; bucket** hiearchy, we come to individual compilation **units** &ndash; Zig source files which uses a novel `#!zigem "em"` library provided by the **Zig&bull;EM** framework.&thinsp; A special `.em.zig` file extension plus an associated icon visually distinguish a **Zig&bull;EM unit** from "ordinary" Zig sources [`src/*.zig`] depicted [earlier](#fig1).

<figure markdown id="fig3">
![Image info](/assets/fig-003-3.png)
<figcaption>Zig&bull;EM Units 
</figure>

!!! info "We'll soon take a closer look at the `BlinkerP.em.zig` and `FiberP.em.zig` source files."

By design, **Zig&bull;EM** limits its **package &gt; bucket &gt; unit** hiearchy to just three levels.&thinsp; The names chosen for top-level packages and their constituent buckets will, however, often assume a `long.qualified.form` &ndash; used to ensure a measure of uniqueness and durability.

!!! bulb "A hierarchical namespace for buckets and packages"

    **Zig&bull;EM** favors a namespace hierarchy when labeling individual **buckets** and **packages**, in which the supplier has a globally-unique _prefix_&thinsp; [`#!zigem "org.<domain>"`, `#!zigem "git.<userid>"`, etc&thinsp;] used in these element names.

    Having said that, buckets and packages supplied by **The EM Foundation** itself [`#!zigem "git.em-foundation"`] will often use a shorter (though still unique) moniker such as `#!zigem "em."` for their namespace prefix.

    Another **Zig&bull;EM** convention:&nbsp; names ascribed to **buckets** should themselves remain globally-unique &ndash; independent of their containing **package(s)**, which also should have unique names.
    
    While the `#!zigem "em.arch.arm"` **bucket** lives in the `#!zigem "em.core"` **package**, a third-party [`#!zigem "git.biosbob"`] could also supply a package (labeled with their own prefix) that contains buckets with the same legacy `#!zigem "em.**"` names.

As we'll see shortly, individual **Zig&bull;EM** source files use a special `#!zigem em.import` operator to reference other units found in the workspace.&thinsp; By design, each unit has a _canonical name_&thinsp; of the form <code>**bucket/Unit**</code>:&nbsp; {[ze,kt]em.examples.basic/BlinkerP}, {[ze,kt]ti.distro.cc23xx/BoardC}, etc.

While **buckets** ultimately reside within **packages**, individual `.em.zig` source files should never reference the latter by name.&thinsp; **Zig&bull;EM** units in fact remain oblivious to any package(s) containing their own bucket as well as other <code>**bucket/Unit**</code> elements they may import.

In essence, **packages** provide a delivery vehicle for <code>**bucket/Unit**</code> content.&thinsp; Each package has a manifest (`zigem-package.ini`) which in general names other packages upon which it depends.&thinsp; **Zig&bull;EM** topologically sorts the (acyclic) dependency relation amongst all packages in the workspace, yielding a search path used when resolving <code>**bucket/Unit**</code> references.

!!! zig "Terminology&thinsp;:: **Zig&bull;EM** = Zig + EM"

    Mapping the original [EM language](https://docs.openem.org/) into Zig can lead to _terminology clashes_, in which elements like **package** have distinct meanings in each language domain.&thinsp; EM, for instance, featured a **bundle > package > unit** hierarchy.&thinsp; For consistency, **Zig&bull;EM** will favor using native Zig nomenclature as much as possible.
    
    Over time, we'll directly leverage [Zig Package Management](https://ziglang.org/download/0.11.0/release-notes.html#Package-Management) mechanisms for delivering buckets of **Zig&bull;EM** content.&thinsp; Said another way, expect each **Zig&bull;EM package** to carry their own `build.zig` and `build.zig.zon` files.&thinsp;  We'll also use Zig **modules** in `build.zig` to define <code>**bucket/Unit**</code> names exposed by the **package**.

    The `workspace/` folder depicted [earlier](#fig2) currently serves as an embryonic prototype &ndash; delivered as part of the `zigem-dev` repository.&thinsp; When we reach **Zig&bull;EM v25.1.0**, however, users will create their own workspace(s) populated with multiple **packages** from multiple suppliers &ndash; each bundling uniquely-labeled <code>**bucket/Unit**</code> content.

## Source code constructs

**Zig&bull;EM units**, as noted earlier, reside in `.em.zig` source files and make use of a special `#!zigem "em"` library.&thinsp; In all other respects, these files conform to the syntax and semantics of Zig.

!!! zig "For Zig-lings and Zig-gurus alike...."

    As you explore the dozens of `.em.zig` files found in the workspace, we recognize that your knowledge of Zig can vary considerably.&thinsp; We'll do our best to literally and figuratively <code class="language-zigem"><span class="nb">highlight</span></code> **Zig&bull;EM**'s unique constructs.

    For those seeing the Zig language for the first time, we strongly recommend [Learning Zig](https://www.openmymind.net/learning_zig/) by Karl Sequin.&thinsp; For those coming from the embedded space with a background in C, you'll find some further motivation behind Zig in this [@avestura](https://avestura.dev/blog/problems-of-c-and-how-zig-addresses-them) blog post as well as this [Zig in 100 Seconds](https://www.youtube.com/watch?v=kxT8-C1vmd4) video.

    And for the Zig gurus:&nbsp; we always welcome your insightful comments at [ziggit.dev](https://ziggit.dev/t/introducing-zig-em/5794) on how to best leverage the underlying language in implementing the core concepts and constructs of the **Zig&bull;EM** framework.


To begin, let's focus on the {[ze,kt]em.examples.basic/BlinkerP} program which illustrates some rudimentary constructs commonly found in a **Zig&bull;EM unit**:

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

Even with no prior knowledge of the Zig language, the behavior of the "main" function between lines {[lr,0,8]} and {[lr,0,15]} should seem obvious &ndash; toggling `#!zigem AppLed#t` ten times every half-second.

Standing back, the first two lines of this file serve as boilerplate which you'll find in _every_&thinsp; **Zig&bull;EM unit:**&nbsp; line {[lr,0,1]} imports our special `#!zigem "em"` library, while line {[lr,0,2]} declares this unit's role as an `#!zigem em.module` and binds a corresponding object to the `#!zigem em__U` framework constant.

!!! em "language keywords versus framework operators" 

    The [EM language](https://docs.openem.org/intro/) introduced the keywords {[ze,k]module}, {[ze,k]interface}, {[ze,k]composite}, and {[ze,k]template} to declare the role played by a specific unit;&thinsp; the **Zig&bull;EM** framework uses its operators `#!zigem em.module`, `#!zigem em.interface`, etc. for a similar purpose.&thinsp;  While **Zig&bull;EM modules** predominate, you will see other sorts of units in due course.

Lines {[lr,0,4]}&ndash;{[lr,0,5]} use the framework's `#!zigem em.import` operator to access {[ze,kt]em.mcu/Common}, as well as the `#!zigem BoardC#t` (**composite**) unit located in a _logical_&thinsp; bucket named {[ze,kt]em__distro}.(1) The `#!zigem BoardC#t` **composite** in turn aggregates a large number of **modules** featuring hardware-specific implementations [{[ze,kt]AppLed}] of hardware-independent **interfaces** [{[ze,kt]em.hal/AppLedI}]&thinsp;.
{ .annotate }

1. currently bound to {[ze,kt]ti.distro.cc23xx} within our workspace's `zigem.ini` configuration file

Finally, the {[ze,nt]EM_TARG} structure defined at line {[lr,0,7]} introduces a new _lexical scope_ containing other Zig declarations (constants, types, variables, functions).&thinsp; We'll explain the role of this special `#!zigem struct` once we examine the lengthier {[ze,kt]em.examples.basic/FiberP} program:

```zigem linenums="1" title="em.examples.basic/FiberP.em.zig"
pub const em = @import("../../zigem/em.zig");
pub const em__U = em.module(@This(), .{});
pub const em__C = em__U.config(EM__CONFIG);

pub const EM__CONFIG = struct {
    blinkF: em.Param(FiberMgr#t.Obj#t),
};

pub const AppLed#t = em.import.@"em__distro/BoardC"#t.AppLed#t;
pub const Common#t = em.import.@"em.mcu/Common"#t;
pub const FiberMgr#t = em.import.@"em.utils/FiberMgr"#t;

pub const EM__META = struct {
    //
    pub fn em__constructH() void {
        const blinkF = FiberMgr#t.createH#f(em__U.fxn("blinkFB", FiberMgr#t.BodyArg#t));
        em__C.blinkF.set#f(blinkF);
    }
};

pub const EM__TARG = struct {
    //
    const blinkF = em__C.blinkF;

    pub fn em__run() void {
        blinkF.post#f();
        FiberMgr.run#f();
    }

    var count: u8 = 5;

    pub fn blinkFB#f(_: FiberMgr#t.BodyArg#t) void {
        em.@"%%[d]"();
        count -= 1;
        if (count == 0) em.halt();
        AppLed#t.on#f();
        Common#t.BusyWait#t.wait#f(100_000);
        AppLed#t.off#f();
        Common#t.BusyWait#t.wait#f(100_000);
        blinkF.post#f();
    }
};
```
This sample program illustrates basic use of {[ze,kt]em.utils/FiberMgr} &ndash; a module delivered within the {[ze,kt]em.core} package, and which manages lightweight threads of type {[ze,kt]FiberMgr.Obj} using a **factory** design pattern applied often within **Zig&bull;EM**.

Looking first at the features declared and defined within the {[ze,nt]EM__TARG} scope, we find:

<span class="em-small">
**line** {[lr,1,23]} &mdash; the constant {[ze,n]blinkF}, which references a {[ze,kt]Fiber.Obj} created earlier in the program<br>
**line** {[lr,1,25]} &mdash; the framework function {[ze,nb]em__run}, which serves as this example's runtime entry-point<br>
**line** {[lr,1,30]} &mdash; the variable {[ze,n]count}, used to track the number of times the program must blink {[ze,kt]AppLed}<br>
**line** {[lr,1,32]} &mdash; the function {[ze,nf]blinkFB}, which represents the code executed upon activating the {[ze,n]blinkF} fiber<br>
</span>

We'll fill in some more details after we examine the top-half of {[ze,kt]em.examples.basic/FiberP}.

Complementing {[ze,nt]EM__TARG}, the {[ze,kt]FiberP} program also declares {[ze,nt]EM__META} beginning at line {[lr,1,13]}.&thinsp; Here too, this special {[ze,kr]struct} can contain declarations and definitions within its scope:

<span class="em-small">
**line** {[lr,1,15]} &mdash; the framework function {[ze,nb]em__constructH}, which creates the {[ze,n]blinkF} fiber used later in the program<br>
**line** {[lr,1,16]} &mdash; {[ze,kt]FiberMgr}.{[ze,nf]createH} also binds our (runtime) {[ze,nf]blinkFB} function to the newly-created {[ze,n]blinkF} fiber  
</span>

To complete the picture, line {[lr,1,5]} of the {[ze,kt]FiberP} program defines a special {[ze,nt]EM__CONFIG} structure &ndash; an instance of which the program assigns to the {[ze,nb]EM__C} framework constant using more boilerplate code back at line {[lr,1,3]}.

!!! info "VS Code snippets"

    The `vscode.zigem` extension includes boilerplate code which you can inject into new **units** within your workspace.&thinsp; Invoke **Command Palette > Snippets: Fill File with Snippet** on an empty `.em.zig` file to experiment.

To appreciate the pivotal role played by the {[ze,nb]EM__C}`.`{[ze,n]blinkF} field throughout our {[ze,kt]FiberP} example, we'll need to examine how the **Zig&bull;EM** framework transforms the `FiberP.em.zig` source file into an executable program image.

## Program compilation

Let's now compile the {[ze,kt]em.examples.basic/FiberP} program, using the framework's {[sh]zigem} command first seen [here](/post-002/#zigem-command):

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][zigem-dev/workspace]}
$ {[sp,em-color-orange]zigem compile -f em.core/em.examples.basic/FiberP.em.zig}
compiling META ...
    board: LP_EM_CC2340R5
    setup: ti.cc23xx://default
compiling TARG ...
    image sha: 93aad9c9
    image size: text (1560) + const (0) + data (40) + bss (4)
done in 6.96 seconds</code></pre></div>

You'll immediately notice that `zigem` compiles the program <u><i>twice</i></u>&nbsp;:&nbsp; once for the **META** domain, and then again for the **TARG** domain.

<div markdown class="em-ol">

The **META** compilation stage processes all source code from lines {[lr,1,1]}&ndash;{[lr,1,19]}, effectively merging the {[ze,nt]EM__META} declarations into the top-level file scope.&thinsp;

The **TARG** compilation stage follows suit, combining common declarations [{[lr,1,1]}&ndash;{[lr,1,11]}] with {[ze,nt]EM__TARG} declarations [{[lr,1,21]}&ndash;{[lr,1,42]}] as input for the underlying Zig compiler.

</div>

While diving into the implementation details of the {[sh]zigem} command lies well beyond the scope of this introductory article, we'll give you a quick peek into the **Zig&bull;EM** "basement" where most of the magic occurs.

!!! zig "For those in the know, just follow the trail heading out from `build.zig` and `src/main.zig`&thinsp;...."

To start, invoke the {[sh]zigem clean} command followed by {[sh]zigem refresh}.&thinsp; Your workspace should now reveal two additional elements generated by the framework:

<figure markdown id="fig4">
![Image info](/assets/fig-003-4.png)
<figcaption>Generated Elements 
</figure>

The `.zigem-main.zig` file provides entry points for the **META** and **TARG** compilatiion stages, which at this point respectively reference _empty_ `zigem/meta.zig` and `zigem/targ.zig` files.

You'll find the "interesting" code generated at this stage in files like `imports.zig`, which reflects an upfront discovery of all **package > bucket > unit** elements in the workspace.

!!! zig "You'll also find a `makefile`, whose recipes will eventually migrate into (generated) `build.zig` files."

By invoking {[sh]zigem compile} with its {[sh]-m} [{[sh]--meta}] option, we can better appreciate the role played by this initial compilation stage.

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][zigem-dev/workspace]}
$ {[sp,em-color-orange]zigem compile -f em.core/em.examples.basic/FiberP.em.zig -m}
compiling META ...
    board: LP_EM_CC2340R5
    setup: ti.cc23xx://default
done in 4.73 seconds</code></pre></div>

Before compilation begins, the framework populates `zigem/meta.zig` with code that will execute our new **META** program &ndash; rooted at the {[ze,kt]em.examples.basic/FiberP} unit and incorporating all other units (recursively) reached through {[ze,nb]em.import}.

Next, the framework invokes the Zig compiler using the {[sh]zig build-exe} command and then runs the `zigem/out/meta-main` executable image output by the compiler.&thinsp; The {[sh]meta} goal inside `zigem/makefile` currently codifies the steps used in this process.

!!! bulb "If not obvious, **META** programs run on your <u>host</u> PC &mdash; and not on resource-constrained target HW&thinsp;!!!"

Functions like {[ze,nb]em__constructH} [&thinsp;defined in the {[ze,kt]FiberP} {[ze,nt]EM__META} scope at {[lr,1,13]}] enjoy execution in an environment with virtually unlimited memory and processing resources, as well as access to the host's file system or even the internet if necessary.

In general, **META** programs declare **config parameters** as fields within per-unit {[ze,nt]EM__CONFIG} structures [{[lr,1,5]}] and modify their values [{[lr,1,17]}] via local definitions of {[ze,nb]em__C}.&thinsp; Ultimately, **Zig&bull;EM** writes the final state of all program config parameters into an updated `zigem/targ.zig` file.

In general, **META** programs declare **config parameters** as fields within per-unit {[ze,nt]EM__CONFIG} structures [{[lr,1,5]}] and modify their values [{[lr,1,17]}] via local definitions of {[ze,nb]em__C}.&thinsp; Ultimately, **Zig&bull;EM** updates its `zigem/targ.zig` file to reflect the final state of all program config parameters.

!!! info "A **config parameter** acts like a {[ze,kr]var} in your **META** program, but like a {[ze,kr]const} in your **TARG** program."

The downstream compilation of {[ze,kt]FiberP} for the **TARG** domain uses a public {[ze,nf]exec} function defined at the bottom of `zigem/targ.zig` as the runtime entry-point.&thinsp; After initializing the target hardware(1){[ze,nf]exec} will call the {[ze,nb]em__run} function [{[lr,1,25]}] defined in {[ze,kt]BlinkerP}.
{ .annotate }

1. via special function like {[ze,nb]em__reset} and {[ze,nb]em__startup}<br>defined in lower-level program units

To summarize:&nbsp; We have a hosted upstream **META** program that outputs constant data consumed by a downstream (cross-compiled) **TARG** program.  This novel two-stage build flow ultimately yields _highly-optimized_&thinsp; executable images for resource-constrained MCU platforms:

To summarize:

<div markdown class="em-small">

{[sb]}&nbsp; a hosted upstream **META** program manipulates **CONFIG** parameters as variables<br>
{[sb]}&nbsp; a downstream **TARG** program consumes these (constant) parameters when cross-compiled<br>
{[sb]}&nbsp; a novel build flow which ultimately yields _highly-optimized_&thinsp; firmware  for resource-constrained MCUs

</div>

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][zigem-dev/workspace]}
$ {[sp,em-color-orange]zigem compile -f em.core/em.examples.basic/FiberP.em.zig}
compiling META ...
    board: LP_EM_CC2340R5
    setup: ti.cc23xx://default
compiling TARG ...
    image sha: 93aad9c9
    image size: text (1560) + const (0) + data (40) + bss (4)
done in 6.96 seconds</code></pre></div>


## Further exploration

Depending upon your background and interests, we present you with several different paths for increasing your understanding of the **Zig&bull;EM** framework:

!!! tip "More sample programs..."

    &thinsp;{[sb]} &nbsp; visit other sample programs in the {[ze,kt]em.examples.basic} bucket<br>
    &thinsp;{[sb]} &nbsp; load these programs onto target hardware, following [these](/post-002/#exploring-zigem) instructions


!!! bulb "Go deep"

    &thinsp;{[sb]} &nbsp; familiarize yourself with the other {[ze,kt]em.&ast;&ast;} buckets, as well as the {[ze,kt]ti.&ast;&ast;} content<br>
    &thinsp;{[sb]} &nbsp; starting with {[ze,kt]AppLed}, plumb down through all units contributing to its implementation 

!!! zig "Behind the curtain..."

    &thinsp;{[sb]} &nbsp; get dirty inside of `em.zig` and `meta-main.zig`, found in the {[ze,kt]em.lang} bucket<br>
    &thinsp;{[sb]} &nbsp; offer up guidance on how to better leverage the Zig language and its build system

{[hc]}
