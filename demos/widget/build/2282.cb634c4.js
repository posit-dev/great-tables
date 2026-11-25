"use strict";(self.rspackChunk_JUPYTERLAB_CORE_OUTPUT=self.rspackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[2282],{12369(e,t,o){function r(e,t,o){return isNaN(e)||e<=t?t:e>=o?o:e}function a(e,t,o){return isNaN(e)||e<=t?0:e>=o?1:e/(o-t)}function i(e,t,o){return isNaN(e)?t:t+e*(o-t)}function l(e){return Math.PI/180*e}function s(e,t,o){return isNaN(e)||e<=0?t:e>=1?o:t+e*(o-t)}function n(e,t,o){if(e<=0)return t%360;if(e>=1)return o%360;let r=(t-o+360)%360;return r<=(o-t+360)%360?(t-r*e+360)%360:(t+r*e+360)%360}function c(e,t){let o=Math.pow(10,t);return Math.round(e*o)/o}o.r(t),o.d(t,{Accordion:()=>o8,AccordionItem:()=>o4,Anchor:()=>rd,AnchoredRegion:()=>rp,Avatar:()=>rv,Badge:()=>rw,Breadcrumb:()=>rC,BreadcrumbItem:()=>rD,Button:()=>rL,Card:()=>rI,Checkbox:()=>rM,Combobox:()=>rW,DataGrid:()=>r1,DataGridCell:()=>rJ,DataGridRow:()=>rQ,DateField:()=>r8,DelegatesARIAToolbar:()=>iD,DesignSystemProvider:()=>al,Dialog:()=>ah,DirectionalStyleSheetBehavior:()=>rb,Disclosure:()=>ag,Divider:()=>am,FoundationToolbar:()=>iV,Icon:()=>rB,Listbox:()=>a$,Menu:()=>aw,MenuItem:()=>aC,NumberField:()=>aD,Option:()=>az,PaletteRGB:()=>ec,Picker:()=>iY,PickerList:()=>i1,PickerListItem:()=>i5,PickerMenu:()=>iJ,PickerMenuOption:()=>iQ,Progress:()=>aH,ProgressRing:()=>aI,Radio:()=>aM,RadioGroup:()=>a_,Search:()=>aY,Select:()=>aJ,Skeleton:()=>a0,Slider:()=>a3,SliderLabel:()=>it,StandardLuminance:()=>A,SwatchRGB:()=>I,Switch:()=>ia,Tab:()=>ih,TabPanel:()=>is,Tabs:()=>ig,TextArea:()=>iv,TextField:()=>iy,Toolbar:()=>iT,Tooltip:()=>iB,TreeItem:()=>iA,TreeView:()=>iE,accentColor:()=>tm,accentFillActive:()=>tN,accentFillActiveDelta:()=>eJ,accentFillFocus:()=>tO,accentFillFocusDelta:()=>eK,accentFillHover:()=>tH,accentFillHoverDelta:()=>eZ,accentFillRecipe:()=>tB,accentFillRest:()=>tL,accentFillRestDelta:()=>eY,accentForegroundActive:()=>tJ,accentForegroundActiveDelta:()=>e1,accentForegroundFocus:()=>tK,accentForegroundFocusDelta:()=>e2,accentForegroundHover:()=>tZ,accentForegroundHoverDelta:()=>e0,accentForegroundRecipe:()=>tX,accentForegroundRest:()=>tY,accentForegroundRestDelta:()=>eQ,accentPalette:()=>tv,accordionItemStyles:()=>o3,accordionStyles:()=>o5,addJupyterLabThemeChangeListener:()=>oK,allComponents:()=>i3,anchorStyles:()=>rc,anchoredRegionStyles:()=>ru,applyJupyterTheme:()=>o1,avatarStyles:()=>rm,badgeStyles:()=>ry,baseHeightMultiplier:()=>ex,baseHorizontalSpacingMultiplier:()=>ey,baseLayerLuminance:()=>ew,bodyFont:()=>e$,breadcrumbItemStyles:()=>rV,breadcrumbStyles:()=>rF,buttonStyles:()=>rj,cardStyles:()=>rO,checkboxStyles:()=>rP,checkboxTemplate:()=>rA,comboboxStyles:()=>rq,controlCornerRadius:()=>ek,dataGridCellStyles:()=>rZ,dataGridRowStyles:()=>rY,dataGridStyles:()=>rX,dateFieldStyles:()=>ae,dateFieldTemplate:()=>at,density:()=>eF,designSystemProviderStyles:()=>an,designSystemProviderTemplate:()=>as,designUnit:()=>eC,dialogStyles:()=>ad,direction:()=>eV,disabledOpacity:()=>eD,disclosureStyles:()=>ap,dividerStyles:()=>af,elementScale:()=>eS,errorColor:()=>oV,errorFillActive:()=>oB,errorFillFocus:()=>oL,errorFillHover:()=>oz,errorFillRecipe:()=>oT,errorFillRest:()=>oj,errorForegroundActive:()=>oX,errorForegroundFocus:()=>oY,errorForegroundHover:()=>oU,errorForegroundRecipe:()=>oq,errorForegroundRest:()=>oW,errorPalette:()=>oD,fillColor:()=>tz,focusStrokeInner:()=>og,focusStrokeInnerRecipe:()=>op,focusStrokeOuter:()=>ou,focusStrokeOuterRecipe:()=>oh,focusStrokeWidth:()=>ej,foregroundOnAccentActive:()=>tM,foregroundOnAccentActiveLarge:()=>tW,foregroundOnAccentFocus:()=>tG,foregroundOnAccentFocusLarge:()=>tU,foregroundOnAccentHover:()=>tA,foregroundOnAccentHoverLarge:()=>tq,foregroundOnAccentLargeRecipe:()=>tE,foregroundOnAccentRecipe:()=>tR,foregroundOnAccentRest:()=>tP,foregroundOnAccentRestLarge:()=>t_,foregroundOnErrorActive:()=>oR,foregroundOnErrorActiveLarge:()=>oE,foregroundOnErrorFocus:()=>oP,foregroundOnErrorFocusLarge:()=>o_,foregroundOnErrorHover:()=>oI,foregroundOnErrorHoverLarge:()=>oG,foregroundOnErrorLargeRecipe:()=>oA,foregroundOnErrorRecipe:()=>oN,foregroundOnErrorRest:()=>oO,foregroundOnErrorRestLarge:()=>oM,heightNumberAsToken:()=>oS,horizontalSliderLabelStyles:()=>a8,iconStyles:()=>rz,imgTemplate:()=>r$,isDark:()=>G,jpAccordion:()=>o7,jpAccordionItem:()=>o9,jpAnchor:()=>rh,jpAnchoredRegion:()=>rg,jpAvatar:()=>rx,jpBadge:()=>rk,jpBreadcrumb:()=>rS,jpBreadcrumbItem:()=>rT,jpButton:()=>rH,jpCard:()=>rR,jpCheckbox:()=>rG,jpCombobox:()=>rU,jpDataGrid:()=>r2,jpDataGridCell:()=>rK,jpDataGridRow:()=>r0,jpDateField:()=>ao,jpDesignSystemProvider:()=>ac,jpDialog:()=>au,jpDisclosure:()=>ab,jpDivider:()=>av,jpListbox:()=>ax,jpMenu:()=>ak,jpMenuItem:()=>aS,jpNumberField:()=>aT,jpOption:()=>aB,jpPicker:()=>iZ,jpPickerList:()=>i2,jpPickerListItem:()=>i6,jpPickerMenu:()=>iK,jpPickerMenuOption:()=>i0,jpProgress:()=>aN,jpProgressRing:()=>aR,jpRadio:()=>aG,jpRadioGroup:()=>aq,jpSearch:()=>aZ,jpSelect:()=>aK,jpSkeleton:()=>a1,jpSlider:()=>a4,jpSliderLabel:()=>io,jpSwitch:()=>ii,jpTab:()=>iu,jpTabPanel:()=>ic,jpTabs:()=>ib,jpTextArea:()=>i$,jpTextField:()=>iw,jpToolbar:()=>ij,jpTooltip:()=>iL,jpTreeItem:()=>iM,jpTreeView:()=>i_,listboxStyles:()=>rE,menuItemStyles:()=>aF,menuStyles:()=>ay,neutralColor:()=>tb,neutralFillActive:()=>t2,neutralFillActiveDelta:()=>e3,neutralFillFocus:()=>t5,neutralFillFocusDelta:()=>e4,neutralFillHover:()=>t1,neutralFillHoverDelta:()=>e6,neutralFillInputActive:()=>t9,neutralFillInputActiveDelta:()=>e7,neutralFillInputFocus:()=>t8,neutralFillInputFocusDelta:()=>te,neutralFillInputHover:()=>t4,neutralFillInputHoverDelta:()=>e8,neutralFillInputRecipe:()=>t6,neutralFillInputRest:()=>t3,neutralFillInputRestDelta:()=>e9,neutralFillLayerRecipe:()=>oc,neutralFillLayerRest:()=>od,neutralFillLayerRestDelta:()=>tc,neutralFillRecipe:()=>tQ,neutralFillRest:()=>t0,neutralFillRestDelta:()=>e5,neutralFillStealthActive:()=>oo,neutralFillStealthActiveDelta:()=>tr,neutralFillStealthFocus:()=>or,neutralFillStealthFocusDelta:()=>ta,neutralFillStealthHover:()=>ot,neutralFillStealthHoverDelta:()=>to,neutralFillStealthRecipe:()=>t7,neutralFillStealthRest:()=>oe,neutralFillStealthRestDelta:()=>tt,neutralFillStrongActive:()=>os,neutralFillStrongActiveDelta:()=>ts,neutralFillStrongFocus:()=>on,neutralFillStrongFocusDelta:()=>tn,neutralFillStrongHover:()=>ol,neutralFillStrongHoverDelta:()=>tl,neutralFillStrongRecipe:()=>oa,neutralFillStrongRest:()=>oi,neutralFillStrongRestDelta:()=>ti,neutralForegroundHint:()=>of,neutralForegroundHintRecipe:()=>ob,neutralForegroundRecipe:()=>om,neutralForegroundRest:()=>ov,neutralLayer1:()=>tF,neutralLayer1Recipe:()=>tk,neutralLayer2:()=>tS,neutralLayer2Recipe:()=>tC,neutralLayer3:()=>tD,neutralLayer3Recipe:()=>tV,neutralLayer4:()=>tj,neutralLayer4Recipe:()=>tT,neutralLayerCardContainer:()=>tx,neutralLayerCardContainerRecipe:()=>t$,neutralLayerFloating:()=>tw,neutralLayerFloatingRecipe:()=>ty,neutralPalette:()=>tf,neutralStrokeActive:()=>ow,neutralStrokeActiveDelta:()=>tu,neutralStrokeDividerRecipe:()=>oF,neutralStrokeDividerRest:()=>oC,neutralStrokeDividerRestDelta:()=>tg,neutralStrokeFocus:()=>ok,neutralStrokeFocusDelta:()=>tp,neutralStrokeHover:()=>oy,neutralStrokeHoverDelta:()=>th,neutralStrokeRecipe:()=>o$,neutralStrokeRest:()=>ox,neutralStrokeRestDelta:()=>td,numberFieldStyles:()=>aV,optionStyles:()=>aj,pickerListItemStyles:()=>iX,pickerMenuOptionStyles:()=>iU,pickerMenuStyles:()=>iW,pickerStyles:()=>iq,progressRingStyles:()=>aO,progressStyles:()=>aL,provideJupyterDesignSystem:()=>i4,radioGroupStyles:()=>aE,radioStyles:()=>aP,radioTemplate:()=>aA,searchStyles:()=>aX,selectStyles:()=>r_,skeletonStyles:()=>aQ,sliderLabelStyles:()=>ie,sliderStyles:()=>a6,strokeWidth:()=>eT,switchStyles:()=>ir,tabPanelStyles:()=>il,tabStyles:()=>id,tabsStyles:()=>ip,textAreaStyles:()=>im,textFieldStyles:()=>ix,toolbarStyles:()=>iC,tooltipStyles:()=>iz,treeItemStyles:()=>iP,treeViewStyles:()=>iG,typeRampBaseFontSize:()=>ez,typeRampBaseLineHeight:()=>eB,typeRampMinus1FontSize:()=>eL,typeRampMinus1LineHeight:()=>eH,typeRampMinus2FontSize:()=>eN,typeRampMinus2LineHeight:()=>eO,typeRampPlus1FontSize:()=>eI,typeRampPlus1LineHeight:()=>eR,typeRampPlus2FontSize:()=>eP,typeRampPlus2LineHeight:()=>eA,typeRampPlus3FontSize:()=>eM,typeRampPlus3LineHeight:()=>eG,typeRampPlus4FontSize:()=>eE,typeRampPlus4LineHeight:()=>e_,typeRampPlus5FontSize:()=>eq,typeRampPlus5LineHeight:()=>eW,typeRampPlus6FontSize:()=>eU,typeRampPlus6LineHeight:()=>eX,verticalSliderLabelStyles:()=>a7});class d{constructor(e,t,o,r){this.r=e,this.g=t,this.b=o,this.a="number"!=typeof r||isNaN(r)?1:r}static fromObject(e){return!e||isNaN(e.r)||isNaN(e.g)||isNaN(e.b)?null:new d(e.r,e.g,e.b,e.a)}equalValue(e){return this.r===e.r&&this.g===e.g&&this.b===e.b&&this.a===e.a}toStringHexRGB(){return"#"+[this.r,this.g,this.b].map(this.formatHexValue).join("")}toStringHexRGBA(){return this.toStringHexRGB()+this.formatHexValue(this.a)}toStringHexARGB(){return"#"+[this.a,this.r,this.g,this.b].map(this.formatHexValue).join("")}toStringWebRGB(){return`rgb(${Math.round(i(this.r,0,255))},${Math.round(i(this.g,0,255))},${Math.round(i(this.b,0,255))})`}toStringWebRGBA(){return`rgba(${Math.round(i(this.r,0,255))},${Math.round(i(this.g,0,255))},${Math.round(i(this.b,0,255))},${r(this.a,0,1)})`}roundToPrecision(e){return new d(c(this.r,e),c(this.g,e),c(this.b,e),c(this.a,e))}clamp(){return new d(r(this.r,0,1),r(this.g,0,1),r(this.b,0,1),r(this.a,0,1))}toObject(){return{r:this.r,g:this.g,b:this.b,a:this.a}}formatHexValue(e){let t;return 1===(t=Math.round(r(i(e,0,255),0,255)).toString(16)).length?"0"+t:t}}let h={aliceblue:{r:.941176,g:.972549,b:1},antiquewhite:{r:.980392,g:.921569,b:.843137},aqua:{r:0,g:1,b:1},aquamarine:{r:.498039,g:1,b:.831373},azure:{r:.941176,g:1,b:1},beige:{r:.960784,g:.960784,b:.862745},bisque:{r:1,g:.894118,b:.768627},black:{r:0,g:0,b:0},blanchedalmond:{r:1,g:.921569,b:.803922},blue:{r:0,g:0,b:1},blueviolet:{r:.541176,g:.168627,b:.886275},brown:{r:.647059,g:.164706,b:.164706},burlywood:{r:.870588,g:.721569,b:.529412},cadetblue:{r:.372549,g:.619608,b:.627451},chartreuse:{r:.498039,g:1,b:0},chocolate:{r:.823529,g:.411765,b:.117647},coral:{r:1,g:.498039,b:.313725},cornflowerblue:{r:.392157,g:.584314,b:.929412},cornsilk:{r:1,g:.972549,b:.862745},crimson:{r:.862745,g:.078431,b:.235294},cyan:{r:0,g:1,b:1},darkblue:{r:0,g:0,b:.545098},darkcyan:{r:0,g:.545098,b:.545098},darkgoldenrod:{r:.721569,g:.52549,b:.043137},darkgray:{r:.662745,g:.662745,b:.662745},darkgreen:{r:0,g:.392157,b:0},darkgrey:{r:.662745,g:.662745,b:.662745},darkkhaki:{r:.741176,g:.717647,b:.419608},darkmagenta:{r:.545098,g:0,b:.545098},darkolivegreen:{r:.333333,g:.419608,b:.184314},darkorange:{r:1,g:.54902,b:0},darkorchid:{r:.6,g:.196078,b:.8},darkred:{r:.545098,g:0,b:0},darksalmon:{r:.913725,g:.588235,b:.478431},darkseagreen:{r:.560784,g:.737255,b:.560784},darkslateblue:{r:.282353,g:.239216,b:.545098},darkslategray:{r:.184314,g:.309804,b:.309804},darkslategrey:{r:.184314,g:.309804,b:.309804},darkturquoise:{r:0,g:.807843,b:.819608},darkviolet:{r:.580392,g:0,b:.827451},deeppink:{r:1,g:.078431,b:.576471},deepskyblue:{r:0,g:.74902,b:1},dimgray:{r:.411765,g:.411765,b:.411765},dimgrey:{r:.411765,g:.411765,b:.411765},dodgerblue:{r:.117647,g:.564706,b:1},firebrick:{r:.698039,g:.133333,b:.133333},floralwhite:{r:1,g:.980392,b:.941176},forestgreen:{r:.133333,g:.545098,b:.133333},fuchsia:{r:1,g:0,b:1},gainsboro:{r:.862745,g:.862745,b:.862745},ghostwhite:{r:.972549,g:.972549,b:1},gold:{r:1,g:.843137,b:0},goldenrod:{r:.854902,g:.647059,b:.12549},gray:{r:.501961,g:.501961,b:.501961},green:{r:0,g:.501961,b:0},greenyellow:{r:.678431,g:1,b:.184314},grey:{r:.501961,g:.501961,b:.501961},honeydew:{r:.941176,g:1,b:.941176},hotpink:{r:1,g:.411765,b:.705882},indianred:{r:.803922,g:.360784,b:.360784},indigo:{r:.294118,g:0,b:.509804},ivory:{r:1,g:1,b:.941176},khaki:{r:.941176,g:.901961,b:.54902},lavender:{r:.901961,g:.901961,b:.980392},lavenderblush:{r:1,g:.941176,b:.960784},lawngreen:{r:.486275,g:.988235,b:0},lemonchiffon:{r:1,g:.980392,b:.803922},lightblue:{r:.678431,g:.847059,b:.901961},lightcoral:{r:.941176,g:.501961,b:.501961},lightcyan:{r:.878431,g:1,b:1},lightgoldenrodyellow:{r:.980392,g:.980392,b:.823529},lightgray:{r:.827451,g:.827451,b:.827451},lightgreen:{r:.564706,g:.933333,b:.564706},lightgrey:{r:.827451,g:.827451,b:.827451},lightpink:{r:1,g:.713725,b:.756863},lightsalmon:{r:1,g:.627451,b:.478431},lightseagreen:{r:.12549,g:.698039,b:.666667},lightskyblue:{r:.529412,g:.807843,b:.980392},lightslategray:{r:.466667,g:.533333,b:.6},lightslategrey:{r:.466667,g:.533333,b:.6},lightsteelblue:{r:.690196,g:.768627,b:.870588},lightyellow:{r:1,g:1,b:.878431},lime:{r:0,g:1,b:0},limegreen:{r:.196078,g:.803922,b:.196078},linen:{r:.980392,g:.941176,b:.901961},magenta:{r:1,g:0,b:1},maroon:{r:.501961,g:0,b:0},mediumaquamarine:{r:.4,g:.803922,b:.666667},mediumblue:{r:0,g:0,b:.803922},mediumorchid:{r:.729412,g:.333333,b:.827451},mediumpurple:{r:.576471,g:.439216,b:.858824},mediumseagreen:{r:.235294,g:.701961,b:.443137},mediumslateblue:{r:.482353,g:.407843,b:.933333},mediumspringgreen:{r:0,g:.980392,b:.603922},mediumturquoise:{r:.282353,g:.819608,b:.8},mediumvioletred:{r:.780392,g:.082353,b:.521569},midnightblue:{r:.098039,g:.098039,b:.439216},mintcream:{r:.960784,g:1,b:.980392},mistyrose:{r:1,g:.894118,b:.882353},moccasin:{r:1,g:.894118,b:.709804},navajowhite:{r:1,g:.870588,b:.678431},navy:{r:0,g:0,b:.501961},oldlace:{r:.992157,g:.960784,b:.901961},olive:{r:.501961,g:.501961,b:0},olivedrab:{r:.419608,g:.556863,b:.137255},orange:{r:1,g:.647059,b:0},orangered:{r:1,g:.270588,b:0},orchid:{r:.854902,g:.439216,b:.839216},palegoldenrod:{r:.933333,g:.909804,b:.666667},palegreen:{r:.596078,g:.984314,b:.596078},paleturquoise:{r:.686275,g:.933333,b:.933333},palevioletred:{r:.858824,g:.439216,b:.576471},papayawhip:{r:1,g:.937255,b:.835294},peachpuff:{r:1,g:.854902,b:.72549},peru:{r:.803922,g:.521569,b:.247059},pink:{r:1,g:.752941,b:.796078},plum:{r:.866667,g:.627451,b:.866667},powderblue:{r:.690196,g:.878431,b:.901961},purple:{r:.501961,g:0,b:.501961},red:{r:1,g:0,b:0},rosybrown:{r:.737255,g:.560784,b:.560784},royalblue:{r:.254902,g:.411765,b:.882353},saddlebrown:{r:.545098,g:.270588,b:.07451},salmon:{r:.980392,g:.501961,b:.447059},sandybrown:{r:.956863,g:.643137,b:.376471},seagreen:{r:.180392,g:.545098,b:.341176},seashell:{r:1,g:.960784,b:.933333},sienna:{r:.627451,g:.321569,b:.176471},silver:{r:.752941,g:.752941,b:.752941},skyblue:{r:.529412,g:.807843,b:.921569},slateblue:{r:.415686,g:.352941,b:.803922},slategray:{r:.439216,g:.501961,b:.564706},slategrey:{r:.439216,g:.501961,b:.564706},snow:{r:1,g:.980392,b:.980392},springgreen:{r:0,g:1,b:.498039},steelblue:{r:.27451,g:.509804,b:.705882},tan:{r:.823529,g:.705882,b:.54902},teal:{r:0,g:.501961,b:.501961},thistle:{r:.847059,g:.74902,b:.847059},tomato:{r:1,g:.388235,b:.278431},transparent:{r:0,g:0,b:0,a:0},turquoise:{r:.25098,g:.878431,b:.815686},violet:{r:.933333,g:.509804,b:.933333},wheat:{r:.960784,g:.870588,b:.701961},white:{r:1,g:1,b:1},whitesmoke:{r:.960784,g:.960784,b:.960784},yellow:{r:1,g:1,b:0},yellowgreen:{r:.603922,g:.803922,b:.196078}},u=/^rgb\(\s*((?:(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\s*,\s*){2}(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\s*)\)$/i,p=/^rgba\(\s*((?:(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\s*,\s*){3}(?:0|1|0?\.\d*)\s*)\)$/i,g=/^#((?:[0-9a-f]{6}|[0-9a-f]{3}))$/i,b=/^#((?:[0-9a-f]{8}|[0-9a-f]{4}))$/i;function f(e){let t=g.exec(e);if(null===t)return null;let o=t[1];if(3===o.length){let e=o.charAt(0),t=o.charAt(1),r=o.charAt(2);o=e.concat(e,t,t,r,r)}let r=parseInt(o,16);return isNaN(r)?null:new d(a((0xff0000&r)>>>16,0,255),a((65280&r)>>>8,0,255),a(255&r,0,255),1)}function m(e){let t,o=e.toLowerCase();return g.test(o)?f(o):b.test(o)?function(e){let t=b.exec(e);if(null===t)return null;let o=t[1];if(4===o.length){let e=o.charAt(0),t=o.charAt(1),r=o.charAt(2),a=o.charAt(3);o=e.concat(e,t,t,r,r,a,a)}let r=parseInt(o,16);return isNaN(r)?null:new d(a((0xff0000&r)>>>16,0,255),a((65280&r)>>>8,0,255),a(255&r,0,255),a((0xff000000&r)>>>24,0,255))}(o):u.test(o)?function(e){let t=u.exec(e);if(null===t)return null;let o=t[1].split(",");return new d(a(Number(o[0]),0,255),a(Number(o[1]),0,255),a(Number(o[2]),0,255),1)}(o):p.test(o)?function(e){let t=p.exec(e);if(null===t)return null;let o=t[1].split(",");return 4===o.length?new d(a(Number(o[0]),0,255),a(Number(o[1]),0,255),a(Number(o[2]),0,255),Number(o[3])):null}(o):h.hasOwnProperty(o)&&(t=h[o.toLowerCase()])?new d(t.r,t.g,t.b,t.hasOwnProperty("a")?t.a:void 0):null}class v{constructor(e,t,o){this.h=e,this.s=t,this.l=o}static fromObject(e){return!e||isNaN(e.h)||isNaN(e.s)||isNaN(e.l)?null:new v(e.h,e.s,e.l)}equalValue(e){return this.h===e.h&&this.s===e.s&&this.l===e.l}roundToPrecision(e){return new v(c(this.h,e),c(this.s,e),c(this.l,e))}toObject(){return{h:this.h,s:this.s,l:this.l}}}class ${constructor(e,t,o){this.h=e,this.s=t,this.v=o}static fromObject(e){return!e||isNaN(e.h)||isNaN(e.s)||isNaN(e.v)?null:new $(e.h,e.s,e.v)}equalValue(e){return this.h===e.h&&this.s===e.s&&this.v===e.v}roundToPrecision(e){return new $(c(this.h,e),c(this.s,e),c(this.v,e))}toObject(){return{h:this.h,s:this.s,v:this.v}}}class x{constructor(e,t,o){this.l=e,this.a=t,this.b=o}static fromObject(e){return!e||isNaN(e.l)||isNaN(e.a)||isNaN(e.b)?null:new x(e.l,e.a,e.b)}equalValue(e){return this.l===e.l&&this.a===e.a&&this.b===e.b}roundToPrecision(e){return new x(c(this.l,e),c(this.a,e),c(this.b,e))}toObject(){return{l:this.l,a:this.a,b:this.b}}}x.epsilon=216/24389,x.kappa=24389/27;class y{constructor(e,t,o){this.l=e,this.c=t,this.h=o}static fromObject(e){return!e||isNaN(e.l)||isNaN(e.c)||isNaN(e.h)?null:new y(e.l,e.c,e.h)}equalValue(e){return this.l===e.l&&this.c===e.c&&this.h===e.h}roundToPrecision(e){return new y(c(this.l,e),c(this.c,e),c(this.h,e))}toObject(){return{l:this.l,c:this.c,h:this.h}}}class w{constructor(e,t,o){this.x=e,this.y=t,this.z=o}static fromObject(e){return!e||isNaN(e.x)||isNaN(e.y)||isNaN(e.z)?null:new w(e.x,e.y,e.z)}equalValue(e){return this.x===e.x&&this.y===e.y&&this.z===e.z}roundToPrecision(e){return new w(c(this.x,e),c(this.y,e),c(this.z,e))}toObject(){return{x:this.x,y:this.y,z:this.z}}}function k(e){return .2126*e.r+.7152*e.g+.0722*e.b}function F(e){function t(e){return e<=.03928?e/12.92:Math.pow((e+.055)/1.055,2.4)}return k(new d(t(e.r),t(e.g),t(e.b),1))}w.whitePoint=new w(.95047,1,1.08883);let C=(e,t)=>(e+.05)/(t+.05);function S(e,t){let o=F(e),r=F(t);return o>r?C(o,r):C(r,o)}function V(e){let t=Math.max(e.r,e.g,e.b),o=Math.min(e.r,e.g,e.b),r=t-o,a=0;0!==r&&(a=t===e.r?60*((e.g-e.b)/r%6):t===e.g?60*((e.b-e.r)/r+2):60*((e.r-e.g)/r+4)),a<0&&(a+=360);let i=(t+o)/2,l=0;return 0!==r&&(l=r/(1-Math.abs(2*i-1))),new v(a,l,i)}function D(e,t=1){let o=(1-Math.abs(2*e.l-1))*e.s,r=o*(1-Math.abs(e.h/60%2-1)),a=e.l-o/2,i=0,l=0,s=0;return e.h<60?(i=o,l=r,s=0):e.h<120?(i=r,l=o,s=0):e.h<180?(i=0,l=o,s=r):e.h<240?(i=0,l=r,s=o):e.h<300?(i=r,l=0,s=o):e.h<360&&(i=o,l=0,s=r),new d(i+a,l+a,s+a,t)}function T(e){let t=Math.max(e.r,e.g,e.b),o=t-Math.min(e.r,e.g,e.b),r=0;0!==o&&(r=t===e.r?60*((e.g-e.b)/o%6):t===e.g?60*((e.b-e.r)/o+2):60*((e.r-e.g)/o+4)),r<0&&(r+=360);let a=0;return 0!==t&&(a=o/t),new $(r,a,t)}function j(e){function t(e){return e<=.04045?e/12.92:Math.pow((e+.055)/1.055,2.4)}let o=t(e.r),r=t(e.g),a=t(e.b);return new w(.4124564*o+.3575761*r+.1804375*a,.2126729*o+.7151522*r+.072175*a,.0193339*o+.119192*r+.9503041*a)}function z(e,t=1){function o(e){return e<=.0031308?12.92*e:1.055*Math.pow(e,1/2.4)-.055}return new d(o(3.2404542*e.x-1.5371385*e.y-.4985314*e.z),o(-.969266*e.x+1.8760108*e.y+.041556*e.z),o(.0556434*e.x-.2040259*e.y+1.0572252*e.z),t)}function B(e){return function(e){function t(e){return e>x.epsilon?Math.pow(e,1/3):(x.kappa*e+16)/116}let o=t(e.x/w.whitePoint.x),r=t(e.y/w.whitePoint.y);return new x(116*r-16,500*(o-r),200*(r-t(e.z/w.whitePoint.z)))}(j(e))}function L(e,t=1){let o,r,a,i,l,s,n,c,d;return z((r=(o=(e.l+16)/116)+e.a/500,a=o-e.b/200,i=Math.pow(r,3),l=Math.pow(o,3),s=Math.pow(a,3),n=0,n=i>x.epsilon?i:(116*r-16)/x.kappa,c=0,c=e.l>x.epsilon*x.kappa?l:e.l/x.kappa,d=0,d=s>x.epsilon?s:(116*a-16)/x.kappa,n=w.whitePoint.x*n,c=w.whitePoint.y*c,d=w.whitePoint.z*d,new w(n,c,d)),t)}function H(e){var t=B(e);let o=0;(Math.abs(t.b)>.001||Math.abs(t.a)>.001)&&(o=180/Math.PI*Math.atan2(t.b,t.a)),o<0&&(o+=360);let r=Math.sqrt(t.a*t.a+t.b*t.b);return new y(t.l,r,o)}function N(e,t=1){let o,r;return L((o=0,r=0,0!==e.h&&(o=Math.cos(l(e.h))*e.c,r=Math.sin(l(e.h))*e.c),new x(e.l,o,r)),t)}function O(e,t){let o=e.relativeLuminance>t.relativeLuminance?e:t,r=e.relativeLuminance>t.relativeLuminance?t:e;return(o.relativeLuminance+.05)/(r.relativeLuminance+.05)}let I=Object.freeze({create:(e,t,o)=>new R(e,t,o),from:e=>new R(e.r,e.g,e.b)});class R extends d{constructor(e,t,o){super(e,t,o,1),this.toColorString=this.toStringHexRGB,this.contrast=O.bind(null,this),this.createCSS=this.toColorString,this.relativeLuminance=F(this)}static fromObject(e){return new R(e.r,e.g,e.b)}}function P(e){return I.create(e,e,e)}let A={LightMode:1,DarkMode:.23},M=(-.1+Math.sqrt(.21))/2;function G(e){return e.relativeLuminance<=M}var E,_,q,W,U,X,Y,Z,J,K=o(90932),Q=o(91490);function ee(e,t,o=18){let r=H(e),a=r.c+t*o;return a<0&&(a=0),N(new y(r.l,a,r.h))}function et(e,t){return new d(e.r*t.r,e.g*t.g,e.b*t.b,1)}function eo(e,t){return e<.5?r(2*t*e,0,1):r(1-2*(1-t)*(1-e),0,1)}function er(e,t){return new d(eo(e.r,t.r),eo(e.g,t.g),eo(e.b,t.b),1)}function ea(e,t,o,r){var a,i,l,c,h,u,p,g,b,f;if(isNaN(e)||e<=0)return o;if(e>=1)return r;switch(t){case X.HSL:return D((a=V(o),i=V(r),isNaN(e)||e<=0?a:e>=1?i:new v(n(e,a.h,i.h),s(e,a.s,i.s),s(e,a.l,i.l))));case X.HSV:return function(e,t=1){let o=e.s*e.v,r=o*(1-Math.abs(e.h/60%2-1)),a=e.v-o,i=0,l=0,s=0;return e.h<60?(i=o,l=r,s=0):e.h<120?(i=r,l=o,s=0):e.h<180?(i=0,l=o,s=r):e.h<240?(i=0,l=r,s=o):e.h<300?(i=r,l=0,s=o):e.h<360&&(i=o,l=0,s=r),new d(i+a,l+a,s+a,t)}((l=T(o),c=T(r),isNaN(e)||e<=0?l:e>=1?c:new $(n(e,l.h,c.h),s(e,l.s,c.s),s(e,l.v,c.v))));case X.XYZ:return z((h=j(o),u=j(r),isNaN(e)||e<=0?h:e>=1?u:new w(s(e,h.x,u.x),s(e,h.y,u.y),s(e,h.z,u.z))));case X.LAB:return L((p=B(o),g=B(r),isNaN(e)||e<=0?p:e>=1?g:new x(s(e,p.l,g.l),s(e,p.a,g.a),s(e,p.b,g.b))));case X.LCH:return N((b=H(o),f=H(r),isNaN(e)||e<=0?b:e>=1?f:new y(s(e,b.l,f.l),s(e,b.c,f.c),n(e,b.h,f.h))));default:return isNaN(e)||e<=0?o:e>=1?r:new d(s(e,o.r,r.r),s(e,o.g,r.g),s(e,o.b,r.b),s(e,o.a,r.a))}}(E=U||(U={}))[E.Burn=0]="Burn",E[E.Color=1]="Color",E[E.Darken=2]="Darken",E[E.Dodge=3]="Dodge",E[E.Lighten=4]="Lighten",E[E.Multiply=5]="Multiply",E[E.Overlay=6]="Overlay",E[E.Screen=7]="Screen",(_=X||(X={}))[_.RGB=0]="RGB",_[_.HSL=1]="HSL",_[_.HSV=2]="HSV",_[_.XYZ=3]="XYZ",_[_.LAB=4]="LAB",_[_.LCH=5]="LCH";class ei{constructor(e){if(null==e||0===e.length)throw Error("The stops argument must be non-empty");this.stops=this.sortColorScaleStops(e)}static createBalancedColorScale(e){if(null==e||0===e.length)throw Error("The colors argument must be non-empty");let t=Array(e.length);for(let o=0;o<e.length;o++)0===o?t[o]={color:e[o],position:0}:o===e.length-1?t[o]={color:e[o],position:1}:t[o]={color:e[o],position:o*(1/(e.length-1))};return new ei(t)}getColor(e,t=X.RGB){if(1===this.stops.length||e<=0)return this.stops[0].color;if(e>=1)return this.stops[this.stops.length-1].color;let o=0;for(let t=0;t<this.stops.length;t++)this.stops[t].position<=e&&(o=t);let r=o+1;return r>=this.stops.length&&(r=this.stops.length-1),ea((e-this.stops[o].position)*(1/(this.stops[r].position-this.stops[o].position)),t,this.stops[o].color,this.stops[r].color)}trim(e,t,o=X.RGB){if(e<0||t>1||t<e)throw Error("Invalid bounds");if(e===t)return new ei([{color:this.getColor(e,o),position:0}]);let r=[];for(let o=0;o<this.stops.length;o++)this.stops[o].position>=e&&this.stops[o].position<=t&&r.push(this.stops[o]);if(0===r.length)return new ei([{color:this.getColor(e),position:e},{color:this.getColor(t),position:t}]);r[0].position!==e&&r.unshift({color:this.getColor(e),position:e}),r[r.length-1].position!==t&&r.push({color:this.getColor(t),position:t});let a=t-e,i=Array(r.length);for(let t=0;t<r.length;t++)i[t]={color:r[t].color,position:(r[t].position-e)/a};return new ei(i)}findNextColor(e,t,o=!1,r=X.RGB,a=.005,i=32){isNaN(e)||e<=0?e=0:e>=1&&(e=1);let l=this.getColor(e,r),s=+!o;if(S(l,this.getColor(s,r))<=t)return s;let n=o?0:e,c=o?e:0,d=s,h=0;for(;h<=i;){d=Math.abs(c-n)/2+n;let e=S(l,this.getColor(d,r));if(Math.abs(e-t)<=a)break;e>t?o?n=d:c=d:o?c=d:n=d,h++}return d}clone(){let e=Array(this.stops.length);for(let t=0;t<e.length;t++)e[t]={color:this.stops[t].color,position:this.stops[t].position};return new ei(e)}sortColorScaleStops(e){return e.sort((e,t)=>{let o=e.position,r=t.position;return o<r?-1:+(o>r)})}}class el{constructor(e){this.config=Object.assign({},el.defaultPaletteConfig,e),this.palette=[],this.updatePaletteColors()}updatePaletteGenerationValues(e){let t=!1;for(let o in e)this.config[o]&&(this.config[o].equalValue?this.config[o].equalValue(e[o])||(this.config[o]=e[o],t=!0):e[o]!==this.config[o]&&(this.config[o]=e[o],t=!0));return t&&this.updatePaletteColors(),t}updatePaletteColors(){let e=this.generatePaletteColorScale();for(let t=0;t<this.config.steps;t++)this.palette[t]=e.getColor(t/(this.config.steps-1),this.config.interpolationMode)}generatePaletteColorScale(){let e=V(this.config.baseColor),t=new ei([{position:0,color:this.config.scaleColorLight},{position:.5,color:this.config.baseColor},{position:1,color:this.config.scaleColorDark}]).trim(this.config.clipLight,1-this.config.clipDark),o=t.getColor(0),r=t.getColor(1),a=o,i=r;if(e.s>=this.config.saturationAdjustmentCutoff&&(a=ee(a,this.config.saturationLight),i=ee(i,this.config.saturationDark)),0!==this.config.multiplyLight){let e=et(this.config.baseColor,a);a=ea(this.config.multiplyLight,this.config.interpolationMode,a,e)}if(0!==this.config.multiplyDark){let e=et(this.config.baseColor,i);i=ea(this.config.multiplyDark,this.config.interpolationMode,i,e)}if(0!==this.config.overlayLight){let e=er(this.config.baseColor,a);a=ea(this.config.overlayLight,this.config.interpolationMode,a,e)}if(0!==this.config.overlayDark){let e=er(this.config.baseColor,i);i=ea(this.config.overlayDark,this.config.interpolationMode,i,e)}return this.config.baseScalePosition?new ei(this.config.baseScalePosition<=0?[{position:0,color:this.config.baseColor},{position:1,color:i.clamp()}]:this.config.baseScalePosition>=1?[{position:0,color:a.clamp()},{position:1,color:this.config.baseColor}]:[{position:0,color:a.clamp()},{position:this.config.baseScalePosition,color:this.config.baseColor},{position:1,color:i.clamp()}]):new ei([{position:0,color:a.clamp()},{position:.5,color:this.config.baseColor},{position:1,color:i.clamp()}])}}el.defaultPaletteConfig={baseColor:f("#808080"),steps:11,interpolationMode:X.RGB,scaleColorLight:new d(1,1,1,1),scaleColorDark:new d(0,0,0,1),clipLight:.185,clipDark:.16,saturationAdjustmentCutoff:.05,saturationLight:.35,saturationDark:1.25,overlayLight:0,overlayDark:.25,multiplyLight:0,multiplyDark:0,baseScalePosition:.5},el.greyscalePaletteConfig={baseColor:f("#808080"),steps:11,interpolationMode:X.RGB,scaleColorLight:new d(1,1,1,1),scaleColorDark:new d(0,0,0,1),clipLight:0,clipDark:0,saturationAdjustmentCutoff:0,saturationLight:0,saturationDark:0,overlayLight:0,overlayDark:0,multiplyLight:0,multiplyDark:0,baseScalePosition:.5},el.defaultPaletteConfig.scaleColorLight,el.defaultPaletteConfig.scaleColorDark;class es{constructor(e){this.palette=[],this.config=Object.assign({},es.defaultPaletteConfig,e),this.regenPalettes()}regenPalettes(){let e=this.config.steps;(isNaN(e)||e<3)&&(e=3);let t=new d(.14,.14,.14,1),o=new el(Object.assign(Object.assign({},el.greyscalePaletteConfig),{baseColor:t,baseScalePosition:86/94,steps:e})).palette,r=k(this.config.baseColor),a=V(this.config.baseColor).l,i=this.matchRelativeLuminanceIndex((r+a)/2,o)/(e-1),l=this.matchRelativeLuminanceIndex(.14,o)/(e-1),s=V(this.config.baseColor),n=D(v.fromObject({h:s.h,s:s.s,l:.14})),c=D(v.fromObject({h:s.h,s:s.s,l:.06})),h=[,,,,,];h[0]={position:0,color:new d(1,1,1,1)},h[1]={position:i,color:this.config.baseColor},h[2]={position:l,color:n},h[3]={position:.99,color:c},h[4]={position:1,color:new d(0,0,0,1)};let u=new ei(h);this.palette=Array(e);for(let t=0;t<e;t++){let o=u.getColor(t/(e-1),X.RGB);this.palette[t]=o}}matchRelativeLuminanceIndex(e,t){let o=Number.MAX_VALUE,r=0,a=0,i=t.length;for(;a<i;a++){let i=Math.abs(k(t[a])-e);i<o&&(o=i,r=a)}return r}}function en(e){return G(e)?-1:1}es.defaultPaletteConfig={baseColor:f("#808080"),steps:94};let ec=Object.freeze({create:function(e,t,o){return"number"==typeof e?ec.from(I.create(e,t,o)):ec.from(e)},from:function(e){return!function(e){let t={r:0,g:0,b:0,toColorString:()=>"",contrast:()=>0,relativeLuminance:0};for(let o in t)if(typeof t[o]!=typeof e[o])return!1;return!0}(e)?ed.from(I.create(e.r,e.g,e.b)):ed.from(e)}});class ed{constructor(e,t){this.closestIndexCache=new Map,this.source=e,this.swatches=t,this.reversedSwatches=Object.freeze([...this.swatches].reverse()),this.lastIndex=this.swatches.length-1}colorContrast(e,t,o,r){void 0===o&&(o=this.closestIndexOf(e));let a=this.swatches,i=this.lastIndex,l=o;return void 0===r&&(r=en(e)),-1===r&&(a=this.reversedSwatches,l=i-l),function e(t,o,r=0,a=t.length-1){if(a===r)return t[r];let i=Math.floor((a-r)/2)+r;return o(t[i])?e(t,o,r,i):e(t,o,i+1,a)}(a,o=>O(e,o)>=t,l,i)}get(e){return this.swatches[e]||this.swatches[r(e,0,this.lastIndex)]}closestIndexOf(e){if(this.closestIndexCache.has(e.relativeLuminance))return this.closestIndexCache.get(e.relativeLuminance);let t=this.swatches.indexOf(e);if(-1!==t)return this.closestIndexCache.set(e.relativeLuminance,t),t;let o=this.swatches.reduce((t,o)=>Math.abs(o.relativeLuminance-e.relativeLuminance)<Math.abs(t.relativeLuminance-e.relativeLuminance)?o:t);return t=this.swatches.indexOf(o),this.closestIndexCache.set(e.relativeLuminance,t),t}static from(e){return new ed(e,Object.freeze(new es({baseColor:d.fromObject(e)}).palette.map(e=>{let t=f(e.toStringHexRGB());return I.create(t.r,t.g,t.b)})))}}let eh=I.create(1,1,1),eu=I.create(0,0,0),ep=I.from(f("#808080")),eg=I.from(f("#DA1A5F")),eb=I.from(f("#D32F2F"));function ef(e,t,o,r,a,i){return Math.max(e.closestIndexOf(P(t))+o,r,a,i)}let{create:em}=K.DesignToken;function ev(e){return K.DesignToken.create({name:e,cssCustomPropertyName:null})}let e$=em("body-font").withDefault('aktiv-grotesk, "Segoe UI", Arial, Helvetica, sans-serif'),ex=em("base-height-multiplier").withDefault(10),ey=em("base-horizontal-spacing-multiplier").withDefault(3),ew=em("base-layer-luminance").withDefault(A.DarkMode),ek=em("control-corner-radius").withDefault(4),eF=em("density").withDefault(0),eC=em("design-unit").withDefault(4),eS=em("element-scale").withDefault(0),eV=em("direction").withDefault(Q.O.ltr),eD=em("disabled-opacity").withDefault(.4),eT=em("stroke-width").withDefault(1),ej=em("focus-stroke-width").withDefault(2),ez=em("type-ramp-base-font-size").withDefault("14px"),eB=em("type-ramp-base-line-height").withDefault("20px"),eL=em("type-ramp-minus-1-font-size").withDefault("12px"),eH=em("type-ramp-minus-1-line-height").withDefault("16px"),eN=em("type-ramp-minus-2-font-size").withDefault("10px"),eO=em("type-ramp-minus-2-line-height").withDefault("16px"),eI=em("type-ramp-plus-1-font-size").withDefault("16px"),eR=em("type-ramp-plus-1-line-height").withDefault("24px"),eP=em("type-ramp-plus-2-font-size").withDefault("20px"),eA=em("type-ramp-plus-2-line-height").withDefault("28px"),eM=em("type-ramp-plus-3-font-size").withDefault("28px"),eG=em("type-ramp-plus-3-line-height").withDefault("36px"),eE=em("type-ramp-plus-4-font-size").withDefault("34px"),e_=em("type-ramp-plus-4-line-height").withDefault("44px"),eq=em("type-ramp-plus-5-font-size").withDefault("46px"),eW=em("type-ramp-plus-5-line-height").withDefault("56px"),eU=em("type-ramp-plus-6-font-size").withDefault("60px"),eX=em("type-ramp-plus-6-line-height").withDefault("72px"),eY=ev("accent-fill-rest-delta").withDefault(0),eZ=ev("accent-fill-hover-delta").withDefault(4),eJ=ev("accent-fill-active-delta").withDefault(-5),eK=ev("accent-fill-focus-delta").withDefault(0),eQ=ev("accent-foreground-rest-delta").withDefault(0),e0=ev("accent-foreground-hover-delta").withDefault(6),e1=ev("accent-foreground-active-delta").withDefault(-4),e2=ev("accent-foreground-focus-delta").withDefault(0),e5=ev("neutral-fill-rest-delta").withDefault(7),e6=ev("neutral-fill-hover-delta").withDefault(10),e3=ev("neutral-fill-active-delta").withDefault(5),e4=ev("neutral-fill-focus-delta").withDefault(0),e9=ev("neutral-fill-input-rest-delta").withDefault(0),e8=ev("neutral-fill-input-hover-delta").withDefault(0),e7=ev("neutral-fill-input-active-delta").withDefault(0),te=ev("neutral-fill-input-focus-delta").withDefault(0),tt=ev("neutral-fill-stealth-rest-delta").withDefault(0),to=ev("neutral-fill-stealth-hover-delta").withDefault(5),tr=ev("neutral-fill-stealth-active-delta").withDefault(3),ta=ev("neutral-fill-stealth-focus-delta").withDefault(0),ti=ev("neutral-fill-strong-rest-delta").withDefault(0),tl=ev("neutral-fill-strong-hover-delta").withDefault(8),ts=ev("neutral-fill-strong-active-delta").withDefault(-5),tn=ev("neutral-fill-strong-focus-delta").withDefault(0),tc=ev("neutral-fill-layer-rest-delta").withDefault(3),td=ev("neutral-stroke-rest-delta").withDefault(25),th=ev("neutral-stroke-hover-delta").withDefault(40),tu=ev("neutral-stroke-active-delta").withDefault(16),tp=ev("neutral-stroke-focus-delta").withDefault(25),tg=ev("neutral-stroke-divider-rest-delta").withDefault(8),tb=em("neutral-color").withDefault(ep),tf=ev("neutral-palette").withDefault(e=>ec.from(tb.getValueFor(e))),tm=em("accent-color").withDefault(eg),tv=ev("accent-palette").withDefault(e=>ec.from(tm.getValueFor(e))),t$=ev("neutral-layer-card-container-recipe").withDefault({evaluate:e=>{var t,o,r;return t=tf.getValueFor(e),o=ew.getValueFor(e),r=tc.getValueFor(e),t.get(t.closestIndexOf(P(o))+r)}}),tx=em("neutral-layer-card-container").withDefault(e=>t$.getValueFor(e).evaluate(e)),ty=ev("neutral-layer-floating-recipe").withDefault({evaluate:e=>{var t,o,r;let a;return t=tf.getValueFor(e),o=ew.getValueFor(e),r=tc.getValueFor(e),a=t.closestIndexOf(P(o))-r,t.get(a-r)}}),tw=em("neutral-layer-floating").withDefault(e=>ty.getValueFor(e).evaluate(e)),tk=ev("neutral-layer-1-recipe").withDefault({evaluate:e=>{var t,o;return t=tf.getValueFor(e),o=ew.getValueFor(e),t.get(t.closestIndexOf(P(o)))}}),tF=em("neutral-layer-1").withDefault(e=>tk.getValueFor(e).evaluate(e)),tC=ev("neutral-layer-2-recipe").withDefault({evaluate:e=>{var t,o,r,a,i,l;return t=tf.getValueFor(e),o=ew.getValueFor(e),r=tc.getValueFor(e),a=e5.getValueFor(e),i=e6.getValueFor(e),l=e3.getValueFor(e),t.get(ef(t,o,r,a,i,l))}}),tS=em("neutral-layer-2").withDefault(e=>tC.getValueFor(e).evaluate(e)),tV=ev("neutral-layer-3-recipe").withDefault({evaluate:e=>{var t,o,r,a,i,l;return t=tf.getValueFor(e),o=ew.getValueFor(e),r=tc.getValueFor(e),a=e5.getValueFor(e),i=e6.getValueFor(e),l=e3.getValueFor(e),t.get(ef(t,o,r,a,i,l)+r)}}),tD=em("neutral-layer-3").withDefault(e=>tV.getValueFor(e).evaluate(e)),tT=ev("neutral-layer-4-recipe").withDefault({evaluate:e=>{var t,o,r,a,i,l;return t=tf.getValueFor(e),o=ew.getValueFor(e),r=tc.getValueFor(e),a=e5.getValueFor(e),i=e6.getValueFor(e),l=e3.getValueFor(e),t.get(ef(t,o,r,a,i,l)+2*r)}}),tj=em("neutral-layer-4").withDefault(e=>tT.getValueFor(e).evaluate(e)),tz=em("fill-color").withDefault(e=>tF.getValueFor(e));(q=Y||(Y={}))[q.normal=4.5]="normal",q[q.large=7]="large";let tB=em({name:"accent-fill-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>{var o,r,a,i,l,s,n,c,d;let h,u,p,g;return o=tv.getValueFor(e),r=tf.getValueFor(e),a=t||tz.getValueFor(e),i=eZ.getValueFor(e),l=eJ.getValueFor(e),s=eK.getValueFor(e),n=e5.getValueFor(e),c=e6.getValueFor(e),d=e3.getValueFor(e),h=o.source,u=r.closestIndexOf(a)>=Math.max(n,c,d)?-1:1,g=(p=o.closestIndexOf(h))+-1*u*i,{rest:o.get(g),hover:o.get(p),active:o.get(g+u*l),focus:o.get(g+u*s)}}}),tL=em("accent-fill-rest").withDefault(e=>tB.getValueFor(e).evaluate(e).rest),tH=em("accent-fill-hover").withDefault(e=>tB.getValueFor(e).evaluate(e).hover),tN=em("accent-fill-active").withDefault(e=>tB.getValueFor(e).evaluate(e).active),tO=em("accent-fill-focus").withDefault(e=>tB.getValueFor(e).evaluate(e).focus),tI=e=>(t,o)=>{var r;return r=o||tL.getValueFor(t),r.contrast(eh)>=e?eh:eu},tR=ev("foreground-on-accent-recipe").withDefault({evaluate:(e,t)=>tI(Y.normal)(e,t)}),tP=em("foreground-on-accent-rest").withDefault(e=>tR.getValueFor(e).evaluate(e,tL.getValueFor(e))),tA=em("foreground-on-accent-hover").withDefault(e=>tR.getValueFor(e).evaluate(e,tH.getValueFor(e))),tM=em("foreground-on-accent-active").withDefault(e=>tR.getValueFor(e).evaluate(e,tN.getValueFor(e))),tG=em("foreground-on-accent-focus").withDefault(e=>tR.getValueFor(e).evaluate(e,tO.getValueFor(e))),tE=ev("foreground-on-accent-large-recipe").withDefault({evaluate:(e,t)=>tI(Y.large)(e,t)}),t_=em("foreground-on-accent-rest-large").withDefault(e=>tE.getValueFor(e).evaluate(e,tL.getValueFor(e))),tq=em("foreground-on-accent-hover-large").withDefault(e=>tE.getValueFor(e).evaluate(e,tH.getValueFor(e))),tW=em("foreground-on-accent-active-large").withDefault(e=>tE.getValueFor(e).evaluate(e,tN.getValueFor(e))),tU=em("foreground-on-accent-focus-large").withDefault(e=>tE.getValueFor(e).evaluate(e,tO.getValueFor(e))),tX=em({name:"accent-foreground-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>{let o;return(o=Y.normal,(e,t)=>{var r,a,i,l,s,n;let c,d,h,u,p,g,b,f,m;return r=tv.getValueFor(e),a=t||tz.getValueFor(e),i=eQ.getValueFor(e),l=e0.getValueFor(e),s=e1.getValueFor(e),n=e2.getValueFor(e),h=r.source,u=r.closestIndexOf(h),g=u+(1===(p=en(a))?Math.min(i,l):Math.max(p*i,p*l)),b=r.colorContrast(a,o,g,p),m=(f=r.closestIndexOf(b))+p*Math.abs(i-l),(1===p?i<l:p*i>p*l)?(c=f,d=m):(c=m,d=f),{rest:r.get(c),hover:r.get(d),active:r.get(c+p*s),focus:r.get(c+p*n)}})(e,t)}}),tY=em("accent-foreground-rest").withDefault(e=>tX.getValueFor(e).evaluate(e).rest),tZ=em("accent-foreground-hover").withDefault(e=>tX.getValueFor(e).evaluate(e).hover),tJ=em("accent-foreground-active").withDefault(e=>tX.getValueFor(e).evaluate(e).active),tK=em("accent-foreground-focus").withDefault(e=>tX.getValueFor(e).evaluate(e).focus),tQ=em({name:"neutral-fill-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>{var o,r,a,i,l,s;let n,c;return o=tf.getValueFor(e),r=t||tz.getValueFor(e),a=e5.getValueFor(e),i=e6.getValueFor(e),l=e3.getValueFor(e),s=e4.getValueFor(e),c=(n=o.closestIndexOf(r))>=Math.max(a,i,l,s)?-1:1,{rest:o.get(n+c*a),hover:o.get(n+c*i),active:o.get(n+c*l),focus:o.get(n+c*s)}}}),t0=em("neutral-fill-rest").withDefault(e=>tQ.getValueFor(e).evaluate(e).rest),t1=em("neutral-fill-hover").withDefault(e=>tQ.getValueFor(e).evaluate(e).hover),t2=em("neutral-fill-active").withDefault(e=>tQ.getValueFor(e).evaluate(e).active),t5=em("neutral-fill-focus").withDefault(e=>tQ.getValueFor(e).evaluate(e).focus),t6=em({name:"neutral-fill-input-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>{var o,r,a,i,l,s;let n,c;return o=tf.getValueFor(e),r=t||tz.getValueFor(e),a=e9.getValueFor(e),i=e8.getValueFor(e),l=e7.getValueFor(e),s=te.getValueFor(e),n=en(r),c=o.closestIndexOf(r),{rest:o.get(c-n*a),hover:o.get(c-n*i),active:o.get(c-n*l),focus:o.get(c-n*s)}}}),t3=em("neutral-fill-input-rest").withDefault(e=>t6.getValueFor(e).evaluate(e).rest),t4=em("neutral-fill-input-hover").withDefault(e=>t6.getValueFor(e).evaluate(e).hover),t9=em("neutral-fill-input-active").withDefault(e=>t6.getValueFor(e).evaluate(e).active),t8=em("neutral-fill-input-focus").withDefault(e=>t6.getValueFor(e).evaluate(e).focus),t7=em({name:"neutral-fill-stealth-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>{var o,r,a,i,l,s,n,c;let d,h,u;return o=tf.getValueFor(e),r=t||tz.getValueFor(e),a=tt.getValueFor(e),i=to.getValueFor(e),l=tr.getValueFor(e),s=ta.getValueFor(e),n=e5.getValueFor(e),c=e6.getValueFor(e),d=Math.max(a,i,l,s,n,c,e3.getValueFor(e),e4.getValueFor(e)),u=(h=o.closestIndexOf(r))>=d?-1:1,{rest:o.get(h+u*a),hover:o.get(h+u*i),active:o.get(h+u*l),focus:o.get(h+u*s)}}}),oe=em("neutral-fill-stealth-rest").withDefault(e=>t7.getValueFor(e).evaluate(e).rest),ot=em("neutral-fill-stealth-hover").withDefault(e=>t7.getValueFor(e).evaluate(e).hover),oo=em("neutral-fill-stealth-active").withDefault(e=>t7.getValueFor(e).evaluate(e).active),or=em("neutral-fill-stealth-focus").withDefault(e=>t7.getValueFor(e).evaluate(e).focus),oa=em({name:"neutral-fill-strong-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>{var o,r,a,i,l,s;let n,c,d,h,u;return o=tf.getValueFor(e),r=t||tz.getValueFor(e),a=ti.getValueFor(e),i=tl.getValueFor(e),l=ts.getValueFor(e),s=tn.getValueFor(e),d=en(r),u=(h=o.closestIndexOf(o.colorContrast(r,4.5)))+d*Math.abs(a-i),(1===d?a<i:d*a>d*i)?(n=h,c=u):(n=u,c=h),{rest:o.get(n),hover:o.get(c),active:o.get(n+d*l),focus:o.get(n+d*s)}}}),oi=em("neutral-fill-strong-rest").withDefault(e=>oa.getValueFor(e).evaluate(e).rest),ol=em("neutral-fill-strong-hover").withDefault(e=>oa.getValueFor(e).evaluate(e).hover),os=em("neutral-fill-strong-active").withDefault(e=>oa.getValueFor(e).evaluate(e).active),on=em("neutral-fill-strong-focus").withDefault(e=>oa.getValueFor(e).evaluate(e).focus),oc=ev("neutral-fill-layer-recipe").withDefault({evaluate:(e,t)=>{var o,r,a;let i;return o=tf.getValueFor(e),r=t||tz.getValueFor(e),a=tc.getValueFor(e),i=o.closestIndexOf(r),o.get(i-(i<a?-1*a:a))}}),od=em("neutral-fill-layer-rest").withDefault(e=>oc.getValueFor(e).evaluate(e)),oh=ev("focus-stroke-outer-recipe").withDefault({evaluate:e=>{var t,o;return t=tf.getValueFor(e),o=tz.getValueFor(e),t.colorContrast(o,3.5)}}),ou=em("focus-stroke-outer").withDefault(e=>oh.getValueFor(e).evaluate(e)),op=ev("focus-stroke-inner-recipe").withDefault({evaluate:e=>{var t,o,r;return t=tv.getValueFor(e),o=tz.getValueFor(e),r=ou.getValueFor(e),t.colorContrast(r,3.5,t.closestIndexOf(t.source),-1*en(o))}}),og=em("focus-stroke-inner").withDefault(e=>op.getValueFor(e).evaluate(e)),ob=ev("neutral-foreground-hint-recipe").withDefault({evaluate:e=>{var t,o;return t=tf.getValueFor(e),o=tz.getValueFor(e),t.colorContrast(o,4.5)}}),of=em("neutral-foreground-hint").withDefault(e=>ob.getValueFor(e).evaluate(e)),om=ev("neutral-foreground-recipe").withDefault({evaluate:e=>{var t,o;return t=tf.getValueFor(e),o=tz.getValueFor(e),t.colorContrast(o,14)}}),ov=em("neutral-foreground-rest").withDefault(e=>om.getValueFor(e).evaluate(e)),o$=em({name:"neutral-stroke-recipe",cssCustomPropertyName:null}).withDefault({evaluate:e=>{var t,o,r,a,i,l;let s,n,c;return t=tf.getValueFor(e),o=tz.getValueFor(e),r=td.getValueFor(e),a=th.getValueFor(e),i=tu.getValueFor(e),l=tp.getValueFor(e),s=t.closestIndexOf(o),c=s+(n=en(o))*r,{rest:t.get(c),hover:t.get(c+n*(a-r)),active:t.get(c+n*(i-r)),focus:t.get(c+n*(l-r))}}}),ox=em("neutral-stroke-rest").withDefault(e=>o$.getValueFor(e).evaluate(e).rest),oy=em("neutral-stroke-hover").withDefault(e=>o$.getValueFor(e).evaluate(e).hover),ow=em("neutral-stroke-active").withDefault(e=>o$.getValueFor(e).evaluate(e).active),ok=em("neutral-stroke-focus").withDefault(e=>o$.getValueFor(e).evaluate(e).focus),oF=ev("neutral-stroke-divider-recipe").withDefault({evaluate:(e,t)=>{var o,r,a;return o=tf.getValueFor(e),r=t||tz.getValueFor(e),a=tg.getValueFor(e),o.get(o.closestIndexOf(r)+en(r)*a)}}),oC=em("neutral-stroke-divider-rest").withDefault(e=>oF.getValueFor(e).evaluate(e)),oS=K.DesignToken.create({name:"height-number",cssCustomPropertyName:null}).withDefault(e=>(ex.getValueFor(e)+eF.getValueFor(e))*eC.getValueFor(e)),oV=em("error-color").withDefault(eb),oD=ev("error-palette").withDefault(e=>ec.from(oV.getValueFor(e))),oT=em({name:"error-fill-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>{var o,r,a,i,l,s,n,c,d;let h,u,p,g;return o=oD.getValueFor(e),r=tf.getValueFor(e),a=t||tz.getValueFor(e),i=eZ.getValueFor(e),l=eJ.getValueFor(e),s=eK.getValueFor(e),n=e5.getValueFor(e),c=e6.getValueFor(e),d=e3.getValueFor(e),h=o.source,u=r.closestIndexOf(a)>=Math.max(n,c,d)?-1:1,g=(p=o.closestIndexOf(h))+-1*u*i,{rest:o.get(g),hover:o.get(p),active:o.get(g+u*l),focus:o.get(g+u*s)}}}),oj=em("error-fill-rest").withDefault(e=>oT.getValueFor(e).evaluate(e).rest),oz=em("error-fill-hover").withDefault(e=>oT.getValueFor(e).evaluate(e).hover),oB=em("error-fill-active").withDefault(e=>oT.getValueFor(e).evaluate(e).active),oL=em("error-fill-focus").withDefault(e=>oT.getValueFor(e).evaluate(e).focus),oH=e=>(t,o)=>{var r;return r=o||oj.getValueFor(t),r.contrast(eh)>=e?eh:eu},oN=em({name:"foreground-on-error-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>oH(Y.normal)(e,t)}),oO=em("foreground-on-error-rest").withDefault(e=>oN.getValueFor(e).evaluate(e,oj.getValueFor(e))),oI=em("foreground-on-error-hover").withDefault(e=>oN.getValueFor(e).evaluate(e,oz.getValueFor(e))),oR=em("foreground-on-error-active").withDefault(e=>oN.getValueFor(e).evaluate(e,oB.getValueFor(e))),oP=em("foreground-on-error-focus").withDefault(e=>oN.getValueFor(e).evaluate(e,oL.getValueFor(e))),oA=em({name:"foreground-on-error-large-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>oH(Y.large)(e,t)}),oM=em("foreground-on-error-rest-large").withDefault(e=>oA.getValueFor(e).evaluate(e,oj.getValueFor(e))),oG=em("foreground-on-error-hover-large").withDefault(e=>oA.getValueFor(e).evaluate(e,oz.getValueFor(e))),oE=em("foreground-on-error-active-large").withDefault(e=>oA.getValueFor(e).evaluate(e,oB.getValueFor(e))),o_=em("foreground-on-error-focus-large").withDefault(e=>oA.getValueFor(e).evaluate(e,oL.getValueFor(e))),oq=em({name:"error-foreground-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>{let o;return(o=Y.normal,(e,t)=>{var r,a,i,l,s,n;let c,d,h,u,p,g,b,f,m;return r=oD.getValueFor(e),a=t||tz.getValueFor(e),i=eQ.getValueFor(e),l=e0.getValueFor(e),s=e1.getValueFor(e),n=e2.getValueFor(e),h=r.source,u=r.closestIndexOf(h),g=u+(1==(p=G(a)?-1:1)?Math.min(i,l):Math.max(p*i,p*l)),b=r.colorContrast(a,o,g,p),m=(f=r.closestIndexOf(b))+p*Math.abs(i-l),(1===p?i<l:p*i>p*l)?(c=f,d=m):(c=m,d=f),{rest:r.get(c),hover:r.get(d),active:r.get(c+p*s),focus:r.get(c+p*n)}})(e,t)}}),oW=em("error-foreground-rest").withDefault(e=>oq.getValueFor(e).evaluate(e).rest),oU=em("error-foreground-hover").withDefault(e=>oq.getValueFor(e).evaluate(e).hover),oX=em("error-foreground-active").withDefault(e=>oq.getValueFor(e).evaluate(e).active),oY=em("error-foreground-focus").withDefault(e=>oq.getValueFor(e).evaluate(e).focus),oZ="--jp-layout-color1",oJ=!1;function oK(){let e;oJ||(oJ=!0,e=()=>{new MutationObserver(()=>{o1()}).observe(document.body,{attributes:!0,attributeFilter:["data-jp-theme-name"],childList:!1,characterData:!1}),o1()},"complete"===document.readyState?e():window.addEventListener("load",e))}let oQ=e=>{let t=parseInt(e,10);return isNaN(t)?null:t},o0={"--jp-border-width":{converter:oQ,token:eT},"--jp-border-radius":{converter:oQ,token:ek},[oZ]:{converter:(e,t)=>{let o=m(e);if(!o)return null;{let e=V(o),t=D(v.fromObject({h:e.h,s:e.s,l:.5}));return I.create(t.r,t.g,t.b)}},token:tb},"--jp-brand-color1":{converter:(e,t)=>{let o=m(e);if(!o)return null;{let e=V(o),r=D(v.fromObject({h:e.h,s:e.s,l:e.l+(t?1:-1)*eZ.getValueFor(document.body)/94}));return I.create(r.r,r.g,r.b)}},token:tm},"--jp-error-color1":{converter:(e,t)=>{let o=m(e);if(!o)return null;{let e=V(o),r=D(v.fromObject({h:e.h,s:e.s,l:e.l+(t?1:-1)*eZ.getValueFor(document.body)/94}));return I.create(r.r,r.g,r.b)}},token:oV},"--jp-ui-font-family":{token:e$},"--jp-ui-font-size1":{token:ez}};function o1(){var e;let t=getComputedStyle(document.body),o=document.body.getAttribute("data-jp-theme-light"),r=!1;if(o)r="false"===o;else{let e=t.getPropertyValue(oZ).toString();if(e){let t=m(e);t&&(r=G(I.create(t.r,t.g,t.b)),console.debug(`Theme is ${r?"dark":"light"} based on '${oZ}' value: ${e}.`))}}for(let o in ew.setValueFor(document.body,r?A.DarkMode:A.LightMode),o0){let a=o0[o],i=t.getPropertyValue(o).toString();if(document.body&&""!==i){let t=(null!=(e=a.converter)?e:e=>e)(i.trim(),r);null!==t?a.token.setValueFor(document.body,t):console.error(`Fail to parse value '${i}' for '${o}' as FAST design token.`)}}}var o2=o(21658);let o5=(e,t)=>(0,o2.css)`
  ${(0,K.display)("flex")} :host {
    box-sizing: border-box;
    flex-direction: column;
    font-family: ${e$};
    font-size: ${eL};
    line-height: ${eH};
    color: ${ov};
    border-top: calc(${eT} * 1px) solid ${oC};
  }
`;(W=Z||(Z={})).Canvas="Canvas",W.CanvasText="CanvasText",W.LinkText="LinkText",W.VisitedText="VisitedText",W.ActiveText="ActiveText",W.ButtonFace="ButtonFace",W.ButtonText="ButtonText",W.Field="Field",W.FieldText="FieldText",W.Highlight="Highlight",W.HighlightText="HighlightText",W.GrayText="GrayText";let o6=(0,o2.cssPartial)`(${ex} + ${eF} + ${eS}) * ${eC}`,o3=(e,t)=>(0,o2.css)`
    ${(0,K.display)("flex")} :host {
      box-sizing: border-box;
      font-family: ${e$};
      flex-direction: column;
      font-size: ${eL};
      line-height: ${eH};
      border-bottom: calc(${eT} * 1px) solid
        ${oC};
    }

    .region {
      display: none;
      padding: calc((6 + (${eC} * 2 * ${eF})) * 1px);
    }

    div.heading {
      display: grid;
      position: relative;
      grid-template-columns: calc(${o6} * 1px) auto 1fr auto;
      color: ${ov};
    }

    .button {
      appearance: none;
      border: none;
      background: none;
      grid-column: 3;
      outline: none;
      padding: 0 calc((6 + (${eC} * 2 * ${eF})) * 1px);
      text-align: left;
      height: calc(${o6} * 1px);
      color: currentcolor;
      cursor: pointer;
      font-family: inherit;
    }

    .button:hover {
      color: currentcolor;
    }

    .button:active {
      color: currentcolor;
    }

    .button::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      cursor: pointer;
    }

    /* prettier-ignore */
    .button:${K.focusVisible}::before {
      outline: none;
      border: calc(${ej} * 1px) solid ${tO};
      border-radius: calc(${ek} * 1px);
    }

    :host([expanded]) .region {
      display: block;
    }

    .icon {
      display: flex;
      align-items: center;
      justify-content: center;
      grid-column: 1;
      grid-row: 1;
      pointer-events: none;
      position: relative;
    }

    slot[name='expanded-icon'],
    slot[name='collapsed-icon'] {
      fill: currentcolor;
    }

    slot[name='collapsed-icon'] {
      display: flex;
    }

    :host([expanded]) slot[name='collapsed-icon'] {
      display: none;
    }

    slot[name='expanded-icon'] {
      display: none;
    }

    :host([expanded]) slot[name='expanded-icon'] {
      display: flex;
    }

    .start {
      display: flex;
      align-items: center;
      padding-inline-start: calc(${eC} * 1px);
      justify-content: center;
      grid-column: 2;
      position: relative;
    }

    .end {
      display: flex;
      align-items: center;
      justify-content: center;
      grid-column: 4;
      position: relative;
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      /* prettier-ignore */
      .button:${K.focusVisible}::before {
          border-color: ${Z.Highlight};
        }
      :host slot[name='collapsed-icon'],
      :host([expanded]) slot[name='expanded-icon'] {
        fill: ${Z.ButtonText};
      }
    `));class o4 extends K.AccordionItem{}let o9=o4.compose({baseName:"accordion-item",baseClass:K.AccordionItem,template:K.accordionItemTemplate,styles:o3,collapsedIcon:`
        <svg
            width="20"
            height="20"
            viewBox="0 0 16 16"
            xmlns="http://www.w3.org/2000/svg"
        >
            <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"
            />
        </svg>
    `,expandedIcon:`
        <svg
            width="20"
            height="20"
            viewBox="0 0 16 16"
            xmlns="http://www.w3.org/2000/svg"
        >
            <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                transform="rotate(90,8,8)"
          d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"
            />
        </svg>
    `});class o8 extends K.Accordion{}let o7=o8.compose({baseName:"accordion",baseClass:K.Accordion,template:K.accordionTemplate,styles:o5});function re(e,t,o,r){var a,i=arguments.length,l=i<3?t:null===r?r=Object.getOwnPropertyDescriptor(t,o):r;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)l=Reflect.decorate(e,t,o,r);else for(var s=e.length-1;s>=0;s--)(a=e[s])&&(l=(i<3?a(l):i>3?a(t,o,l):a(t,o))||l);return i>3&&l&&Object.defineProperty(t,o,l),l}let rt=(0,o2.css)`
  ${(0,K.display)("inline-flex")} :host {
    font-family: ${e$};
    outline: none;
    font-size: ${ez};
    line-height: ${eB};
    height: calc(${o6} * 1px);
    min-width: calc(${o6} * 1px);
    background-color: ${t0};
    color: ${ov};
    border-radius: calc(${ek} * 1px);
    fill: currentcolor;
    cursor: pointer;
    margin: calc((${ej} + 2) * 1px);
  }

  .control {
    background: transparent;
    height: inherit;
    flex-grow: 1;
    box-sizing: border-box;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    padding: 0
      max(
        1px,
        calc((14 + (${eC} * (${eF} + ${eS})))) * 1px
      );
    white-space: nowrap;
    outline: none;
    text-decoration: none;
    border: calc(${eT} * 1px) solid transparent;
    color: inherit;
    border-radius: inherit;
    fill: inherit;
    cursor: inherit;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
  }

  :host(:hover) {
    background-color: ${t1};
  }

  :host(:active) {
    background-color: ${t2};
  }

  :host([aria-pressed='true']) {
    box-shadow: inset 0px 0px 2px 2px ${os};
  }

  :host([minimal]),
  :host([scale='xsmall']) {
    --element-scale: -4;
  }

  :host([scale='small']) {
    --element-scale: -2;
  }

  :host([scale='medium']) {
    --element-scale: 0;
  }

  :host([scale='large']) {
    --element-scale: 2;
  }

  :host([scale='xlarge']) {
    --element-scale: 4;
  }

  /* prettier-ignore */
  .control:${K.focusVisible} {
      outline: calc(${ej} * 1px) solid ${on};
      outline-offset: 2px;
      -moz-outline-radius: 0px;
    }

  .control::-moz-focus-inner {
    border: 0;
  }

  .start,
  .end {
    display: flex;
  }

  .control.icon-only {
    padding: 0;
    line-height: 0;
  }

  ::slotted(svg),
  ::slotted(jp-icon) {
    ${""} width: 16px;
    height: 16px;
    pointer-events: none;
  }

  .start {
    margin-inline-end: 11px;
  }

  .end {
    margin-inline-start: 11px;
  }
`.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
    :host .control {
      background-color: ${Z.ButtonFace};
      border-color: ${Z.ButtonText};
      color: ${Z.ButtonText};
      fill: currentColor;
    }

    :host(:hover) .control {
      forced-color-adjust: none;
      background-color: ${Z.Highlight};
      color: ${Z.HighlightText};
    }

    /* prettier-ignore */
    .control:${K.focusVisible} {
          forced-color-adjust: none;
          background-color: ${Z.Highlight};
          outline-color: ${Z.ButtonText};
          color: ${Z.HighlightText};
        }

    .control:hover,
    :host([appearance='outline']) .control:hover {
      border-color: ${Z.ButtonText};
    }

    :host([href]) .control {
      border-color: ${Z.LinkText};
      color: ${Z.LinkText};
    }

    :host([href]) .control:hover,
        :host([href]) .control:${K.focusVisible} {
      forced-color-adjust: none;
      background: ${Z.ButtonFace};
      outline-color: ${Z.LinkText};
      color: ${Z.LinkText};
      fill: currentColor;
    }
  `)),ro=(0,o2.css)`
  :host([appearance='accent']) {
    background: ${tL};
    color: ${tP};
  }

  :host([appearance='accent']:hover) {
    background: ${tH};
    color: ${tA};
  }

  :host([appearance='accent'][aria-pressed='true']) {
    box-shadow: inset 0px 0px 2px 2px ${tJ};
  }

  :host([appearance='accent']:active) .control:active {
    background: ${tN};
    color: ${tM};
  }

  :host([appearance="accent"]) .control:${K.focusVisible} {
    outline-color: ${tO};
  }
`.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
    :host([appearance='accent']) .control {
      forced-color-adjust: none;
      background: ${Z.Highlight};
      color: ${Z.HighlightText};
    }

    :host([appearance='accent']) .control:hover,
    :host([appearance='accent']:active) .control:active {
      background: ${Z.HighlightText};
      border-color: ${Z.Highlight};
      color: ${Z.Highlight};
    }

    :host([appearance="accent"]) .control:${K.focusVisible} {
      outline-color: ${Z.Highlight};
    }

    :host([appearance='accent'][href]) .control {
      background: ${Z.LinkText};
      color: ${Z.HighlightText};
    }

    :host([appearance='accent'][href]) .control:hover {
      background: ${Z.ButtonFace};
      border-color: ${Z.LinkText};
      box-shadow: none;
      color: ${Z.LinkText};
      fill: currentColor;
    }

    :host([appearance="accent"][href]) .control:${K.focusVisible} {
      outline-color: ${Z.HighlightText};
    }
  `)),rr=(0,o2.css)`
  :host([appearance='error']) {
    background: ${oj};
    color: ${tP};
  }

  :host([appearance='error']:hover) {
    background: ${oz};
    color: ${tA};
  }

  :host([appearance='error'][aria-pressed='true']) {
    box-shadow: inset 0px 0px 2px 2px ${oX};
  }

  :host([appearance='error']:active) .control:active {
    background: ${oB};
    color: ${tM};
  }

  :host([appearance="error"]) .control:${K.focusVisible} {
    outline-color: ${oL};
  }
`.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
    :host([appearance='error']) .control {
      forced-color-adjust: none;
      background: ${Z.Highlight};
      color: ${Z.HighlightText};
    }

    :host([appearance='error']) .control:hover,
    :host([appearance='error']:active) .control:active {
      background: ${Z.HighlightText};
      border-color: ${Z.Highlight};
      color: ${Z.Highlight};
    }

    :host([appearance="error"]) .control:${K.focusVisible} {
      outline-color: ${Z.Highlight};
    }

    :host([appearance='error'][href]) .control {
      background: ${Z.LinkText};
      color: ${Z.HighlightText};
    }

    :host([appearance='error'][href]) .control:hover {
      background: ${Z.ButtonFace};
      border-color: ${Z.LinkText};
      box-shadow: none;
      color: ${Z.LinkText};
      fill: currentColor;
    }

    :host([appearance="error"][href]) .control:${K.focusVisible} {
      outline-color: ${Z.HighlightText};
    }
  `)),ra=(0,o2.css)`
  :host([appearance='hypertext']) {
    font-size: inherit;
    line-height: inherit;
    height: auto;
    min-width: 0;
    background: transparent;
  }

  :host([appearance='hypertext']) .control {
    display: inline;
    padding: 0;
    border: none;
    box-shadow: none;
    border-radius: 0;
    line-height: 1;
  }

  :host a.control:not(:link) {
    background-color: transparent;
    cursor: default;
  }
  :host([appearance='hypertext']) .control:link,
  :host([appearance='hypertext']) .control:visited {
    background: transparent;
    color: ${tY};
    border-bottom: calc(${eT} * 1px) solid ${tY};
  }

  :host([appearance='hypertext']:hover),
  :host([appearance='hypertext']) .control:hover {
    background: transparent;
    border-bottom-color: ${tZ};
  }

  :host([appearance='hypertext']:active),
  :host([appearance='hypertext']) .control:active {
    background: transparent;
    border-bottom-color: ${tJ};
  }

  :host([appearance="hypertext"]) .control:${K.focusVisible} {
    outline-color: transparent;
    border-bottom: calc(${ej} * 1px) solid ${ou};
    margin-bottom: calc(calc(${eT} - ${ej}) * 1px);
  }
`.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
    :host([appearance='hypertext']:hover) {
      background-color: ${Z.ButtonFace};
      color: ${Z.ButtonText};
    }
    :host([appearance="hypertext"][href]) .control:hover,
        :host([appearance="hypertext"][href]) .control:active,
        :host([appearance="hypertext"][href]) .control:${K.focusVisible} {
      color: ${Z.LinkText};
      border-bottom-color: ${Z.LinkText};
      box-shadow: none;
    }
  `)),ri=(0,o2.css)`
  :host([appearance='lightweight']) {
    background: transparent;
    color: ${tY};
  }

  :host([appearance='lightweight']) .control {
    padding: 0;
    height: initial;
    border: none;
    box-shadow: none;
    border-radius: 0;
  }

  :host([appearance='lightweight']:hover) {
    background: transparent;
    color: ${tZ};
  }

  :host([appearance='lightweight']:active) {
    background: transparent;
    color: ${tJ};
  }

  :host([appearance='lightweight']) .content {
    position: relative;
  }

  :host([appearance='lightweight']) .content::before {
    content: '';
    display: block;
    height: calc(${eT} * 1px);
    position: absolute;
    top: calc(1em + 4px);
    width: 100%;
  }

  :host([appearance='lightweight']:hover) .content::before {
    background: ${tZ};
  }

  :host([appearance='lightweight']:active) .content::before {
    background: ${tJ};
  }

  :host([appearance="lightweight"]) .control:${K.focusVisible} {
    outline-color: transparent;
  }

  :host([appearance="lightweight"]) .control:${K.focusVisible} .content::before {
    background: ${ov};
    height: calc(${ej} * 1px);
  }
`.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
    :host([appearance="lightweight"]) .control:hover,
        :host([appearance="lightweight"]) .control:${K.focusVisible} {
      forced-color-adjust: none;
      background: ${Z.ButtonFace};
      color: ${Z.Highlight};
    }
    :host([appearance="lightweight"]) .control:hover .content::before,
        :host([appearance="lightweight"]) .control:${K.focusVisible} .content::before {
      background: ${Z.Highlight};
    }

    :host([appearance="lightweight"][href]) .control:hover,
        :host([appearance="lightweight"][href]) .control:${K.focusVisible} {
      background: ${Z.ButtonFace};
      box-shadow: none;
      color: ${Z.LinkText};
    }

    :host([appearance="lightweight"][href]) .control:hover .content::before,
        :host([appearance="lightweight"][href]) .control:${K.focusVisible} .content::before {
      background: ${Z.LinkText};
    }
  `)),rl=(0,o2.css)`
  :host([appearance='outline']) {
    background: transparent;
    border-color: ${tL};
  }

  :host([appearance='outline']:hover) {
    border-color: ${tH};
  }

  :host([appearance='outline']:active) {
    border-color: ${tN};
  }

  :host([appearance='outline']) .control {
    border-color: inherit;
  }

  :host([appearance="outline"]) .control:${K.focusVisible} {
    outline-color: ${tO};
  }
`.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
    :host([appearance='outline']) .control {
      border-color: ${Z.ButtonText};
    }
    :host([appearance="outline"]) .control:${K.focusVisible} {
      forced-color-adjust: none;
      background-color: ${Z.Highlight};
      outline-color: ${Z.ButtonText};
      color: ${Z.HighlightText};
      fill: currentColor;
    }
    :host([appearance='outline'][href]) .control {
      background: ${Z.ButtonFace};
      border-color: ${Z.LinkText};
      color: ${Z.LinkText};
      fill: currentColor;
    }
    :host([appearance="outline"][href]) .control:hover,
        :host([appearance="outline"][href]) .control:${K.focusVisible} {
      forced-color-adjust: none;
      outline-color: ${Z.LinkText};
    }
  `)),rs=(0,o2.css)`
  :host([appearance='stealth']),
  :host([appearance='stealth'][disabled]:active),
  :host([appearance='stealth'][disabled]:hover) {
    background: transparent;
  }

  :host([appearance='stealth']:hover) {
    background: ${ot};
  }

  :host([appearance='stealth']:active) {
    background: ${oo};
  }

  :host([appearance='stealth']) .control:${K.focusVisible} {
    outline-color: ${tO};
  }

  /* Make the focus outline displayed within the button if
     it is in a start or end slot; e.g. in a tree item
     This will make the focus outline bounded within the container.
   */
  :host([appearance='stealth'][slot="end"]) .control:${K.focusVisible},
  :host([appearance='stealth'][slot="start"]) .control:${K.focusVisible} {
    outline-offset: -2px;
  }
`.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
    :host([appearance='stealth']),
    :host([appearance='stealth']) .control {
      forced-color-adjust: none;
      background: ${Z.ButtonFace};
      border-color: transparent;
      color: ${Z.ButtonText};
      fill: currentColor;
    }

    :host([appearance='stealth']:hover) .control {
      background: ${Z.Highlight};
      border-color: ${Z.Highlight};
      color: ${Z.HighlightText};
      fill: currentColor;
    }

    :host([appearance="stealth"]:${K.focusVisible}) .control {
      outline-color: ${Z.Highlight};
      color: ${Z.HighlightText};
      fill: currentColor;
    }

    :host([appearance='stealth'][href]) .control {
      color: ${Z.LinkText};
    }

    :host([appearance="stealth"][href]:hover) .control,
        :host([appearance="stealth"][href]:${K.focusVisible}) .control {
      background: ${Z.LinkText};
      border-color: ${Z.LinkText};
      color: ${Z.HighlightText};
      fill: currentColor;
    }

    :host([appearance="stealth"][href]:${K.focusVisible}) .control {
      forced-color-adjust: none;
      box-shadow: 0 0 0 1px ${Z.LinkText};
    }
  `));function rn(e,t){return new K.PropertyStyleSheetBehavior("appearance",e,t)}let rc=(e,t)=>(0,o2.css)`
    ${rt}
  `.withBehaviors(rn("accent",ro),rn("hypertext",ra),rn("lightweight",ri),rn("outline",rl),rn("stealth",rs));class rd extends K.Anchor{appearanceChanged(e,t){this.$fastController.isConnected&&(this.classList.remove(e),this.classList.add(t))}connectedCallback(){super.connectedCallback(),this.appearance||(this.appearance="neutral")}defaultSlottedContentChanged(e,t){let o=this.defaultSlottedContent.filter(e=>e.nodeType===Node.ELEMENT_NODE);1===o.length&&o[0]instanceof SVGElement?this.control.classList.add("icon-only"):this.control.classList.remove("icon-only")}}re([o2.attr],rd.prototype,"appearance",void 0);let rh=rd.compose({baseName:"anchor",baseClass:K.Anchor,template:K.anchorTemplate,styles:rc,shadowOptions:{delegatesFocus:!0}}),ru=(e,t)=>(0,o2.css)`
  :host {
    contain: layout;
    display: block;
  }
`;class rp extends K.AnchoredRegion{}let rg=rp.compose({baseName:"anchored-region",baseClass:K.AnchoredRegion,template:K.anchoredRegionTemplate,styles:ru});class rb{constructor(e,t){this.cache=new WeakMap,this.ltr=e,this.rtl=t}bind(e){this.attach(e)}unbind(e){let t=this.cache.get(e);t&&eV.unsubscribe(t)}attach(e){let t=this.cache.get(e)||new rf(this.ltr,this.rtl,e),o=eV.getValueFor(e);eV.subscribe(t),t.attach(o),this.cache.set(e,t)}}class rf{constructor(e,t,o){this.ltr=e,this.rtl=t,this.source=o,this.attached=null}handleChange({target:e,token:t}){this.attach(t.getValueFor(e))}attach(e){this.attached!==this[e]&&(null!==this.attached&&this.source.$fastController.removeStyles(this.attached),this.attached=this[e],null!==this.attached&&this.source.$fastController.addStyles(this.attached))}}let rm=(e,t)=>(0,o2.css)`
    ${(0,K.display)("flex")} :host {
      position: relative;
      height: var(--avatar-size, var(--avatar-size-default));
      width: var(--avatar-size, var(--avatar-size-default));
      --avatar-size-default: calc(
        (
            (${ex} + ${eF}) * ${eC} +
              ((${eC} * 8) - 40)
          ) * 1px
      );
      --avatar-text-size: ${ez};
      --avatar-text-ratio: ${eC};
    }

    .link {
      text-decoration: none;
      color: ${ov};
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      min-width: 100%;
    }

    .square {
      border-radius: calc(${ek} * 1px);
      min-width: 100%;
      overflow: hidden;
    }

    .circle {
      border-radius: 100%;
      min-width: 100%;
      overflow: hidden;
    }

    .backplate {
      position: relative;
      display: flex;
      background-color: ${tL};
    }

    .media,
    ::slotted(img) {
      max-width: 100%;
      position: absolute;
      display: block;
    }

    .content {
      font-size: calc(
        (
            var(--avatar-text-size) +
              var(--avatar-size, var(--avatar-size-default))
          ) / var(--avatar-text-ratio)
      );
      line-height: var(--avatar-size, var(--avatar-size-default));
      display: block;
      min-height: var(--avatar-size, var(--avatar-size-default));
    }

    ::slotted(${e.tagFor(K.Badge)}) {
      position: absolute;
      display: block;
    }
  `.withBehaviors(new rb((0,o2.css)`
  ::slotted(${e.tagFor(K.Badge)}) {
    right: 0;
  }
`,(0,o2.css)`
  ::slotted(${e.tagFor(K.Badge)}) {
    left: 0;
  }
`));class rv extends K.Avatar{}re([(0,o2.attr)({attribute:"src"})],rv.prototype,"imgSrc",void 0),re([o2.attr],rv.prototype,"alt",void 0);let r$=(0,o2.html)`
  ${(0,o2.when)(e=>e.imgSrc,(0,o2.html)`
      <img
        src="${e=>e.imgSrc}"
        alt="${e=>e.alt}"
        slot="media"
        class="media"
        part="media"
      />
    `)}
`,rx=rv.compose({baseName:"avatar",baseClass:K.Avatar,template:K.avatarTemplate,styles:rm,media:r$,shadowOptions:{delegatesFocus:!0}}),ry=(e,t)=>(0,o2.css)`
  ${(0,K.display)("inline-block")} :host {
    box-sizing: border-box;
    font-family: ${e$};
    font-size: ${eL};
    line-height: ${eH};
  }

  .control {
    border-radius: calc(${ek} * 1px);
    padding: calc(((${eC} * 0.5) - ${eT}) * 1px)
      calc((${eC} - ${eT}) * 1px);
    color: ${ov};
    font-weight: 600;
    border: calc(${eT} * 1px) solid transparent;
    background-color: ${t0};
  }

  .control[style] {
    font-weight: 400;
  }

  :host([circular]) .control {
    border-radius: 100px;
    padding: 0 calc(${eC} * 1px);
    height: calc((${o6} - (${eC} * 3)) * 1px);
    min-width: calc((${o6} - (${eC} * 3)) * 1px);
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
  }
`;class rw extends K.Badge{}let rk=rw.compose({baseName:"badge",baseClass:K.Badge,template:K.badgeTemplate,styles:ry}),rF=(e,t)=>(0,o2.css)`
  ${(0,K.display)("inline-block")} :host {
    box-sizing: border-box;
    font-family: ${e$};
    font-size: ${ez};
    line-height: ${eB};
  }

  .list {
    display: flex;
    flex-wrap: wrap;
  }
`;class rC extends K.Breadcrumb{}let rS=rC.compose({baseName:"breadcrumb",baseClass:K.Breadcrumb,template:K.breadcrumbTemplate,styles:rF}),rV=(e,t)=>(0,o2.css)`
    ${(0,K.display)("inline-flex")} :host {
        background: transparent;
        box-sizing: border-box;
        font-family: ${e$};
        font-size: ${ez};
        fill: currentColor;
        line-height: ${eB};
        min-width: calc(${o6} * 1px);
        outline: none;
        color: ${ov}
    }

    .listitem {
        display: flex;
        align-items: center;
        width: max-content;
    }

    .separator {
        margin: 0 6px;
        display: flex;
    }

    .control {
        align-items: center;
        box-sizing: border-box;
        color: ${tY};
        cursor: pointer;
        display: flex;
        fill: inherit;
        outline: none;
        text-decoration: none;
        white-space: nowrap;
    }

    .control:hover {
        color: ${tZ};
    }

    .control:active {
        color: ${tJ};
    }

    .control .content {
        position: relative;
    }

    .control .content::before {
        content: "";
        display: block;
        height: calc(${eT} * 1px);
        left: 0;
        position: absolute;
        right: 0;
        top: calc(1em + 4px);
        width: 100%;
    }

    .control:hover .content::before {
        background: ${tZ};
    }

    .control:active .content::before {
        background: ${tJ};
    }

    .control:${K.focusVisible} .content::before {
        background: ${tK};
        height: calc(${ej} * 1px);
    }

    .control:not([href]) {
        color: ${ov};
        cursor: default;
    }

    .control:not([href]) .content::before {
        background: none;
    }

    .start,
    .end {
        display: flex;
    }

    ::slotted(svg),
    ::slotted(jp-icon) {
        /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
        width: 16px;
        height: 16px;
    }

    .start {
        margin-inline-end: 6px;
    }

    .end {
        margin-inline-start: 6px;
    }
`.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      .control:hover .content::before,
                .control:${K.focusVisible} .content::before {
        background: ${Z.LinkText};
      }
      .start,
      .end {
        fill: ${Z.ButtonText};
      }
    `));class rD extends K.BreadcrumbItem{}let rT=rD.compose({baseName:"breadcrumb-item",baseClass:K.BreadcrumbItem,template:K.breadcrumbItemTemplate,styles:rV,separator:"/",shadowOptions:{delegatesFocus:!0}}),rj=(e,t)=>(0,o2.css)`
    :host([disabled]),
    :host([disabled]:hover),
    :host([disabled]:active) {
      opacity: ${eD};
      background-color: ${t0};
      cursor: ${K.disabledCursor};
    }

    ${rt}
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host([disabled]),
      :host([disabled]) .control,
      :host([disabled]:hover),
      :host([disabled]:active) {
        forced-color-adjust: none;
        background-color: ${Z.ButtonFace};
        outline-color: ${Z.GrayText};
        color: ${Z.GrayText};
        cursor: ${K.disabledCursor};
        opacity: 1;
      }
    `),rn("accent",(0,o2.css)`
        :host([appearance='accent'][disabled]),
        :host([appearance='accent'][disabled]:hover),
        :host([appearance='accent'][disabled]:active) {
          background: ${tL};
        }

        ${ro}
      `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
          :host([appearance='accent'][disabled]) .control,
          :host([appearance='accent'][disabled]) .control:hover {
            background: ${Z.ButtonFace};
            border-color: ${Z.GrayText};
            color: ${Z.GrayText};
          }
        `))),rn("error",(0,o2.css)`
        :host([appearance='error'][disabled]),
        :host([appearance='error'][disabled]:hover),
        :host([appearance='error'][disabled]:active) {
          background: ${oj};
        }

        ${rr}
      `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
          :host([appearance='error'][disabled]) .control,
          :host([appearance='error'][disabled]) .control:hover {
            background: ${Z.ButtonFace};
            border-color: ${Z.GrayText};
            color: ${Z.GrayText};
          }
        `))),rn("lightweight",(0,o2.css)`
        :host([appearance='lightweight'][disabled]:hover),
        :host([appearance='lightweight'][disabled]:active) {
          background-color: transparent;
          color: ${tY};
        }

        :host([appearance='lightweight'][disabled]) .content::before,
        :host([appearance='lightweight'][disabled]:hover) .content::before,
        :host([appearance='lightweight'][disabled]:active) .content::before {
          background: transparent;
        }

        ${ri}
      `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
          :host([appearance='lightweight'].disabled) .control {
            forced-color-adjust: none;
            color: ${Z.GrayText};
          }

          :host([appearance='lightweight'].disabled)
            .control:hover
            .content::before {
            background: none;
          }
        `))),rn("outline",(0,o2.css)`
        :host([appearance='outline'][disabled]),
        :host([appearance='outline'][disabled]:hover),
        :host([appearance='outline'][disabled]:active) {
          background: transparent;
          border-color: ${tL};
        }

        ${rl}
      `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
          :host([appearance='outline'][disabled]) .control {
            border-color: ${Z.GrayText};
          }
        `))),rn("stealth",(0,o2.css)`
        ${rs}
      `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
          :host([appearance='stealth'][disabled]) {
            background: ${Z.ButtonFace};
          }

          :host([appearance='stealth'][disabled]) .control {
            background: ${Z.ButtonFace};
            border-color: transparent;
            color: ${Z.GrayText};
          }
        `)))),rz=(0,o2.css)`
  ${(0,K.display)("inline-block")} :host {
    inline-size: ${o6};
    block-size: ${o6};
  }

  :host svg {
    display: block;
    width: 100%;
    height: 100%;
  }
`,rB=J=class extends o2.FASTElement{static register(e){J.iconsMap.has(e.name)&&console.warn(`Redefining previously loaded icon svgStr. name: ${e.name}, svgStrOld: ${J.iconsMap.get(e.name)}, svgStr: ${e.svgStr}`),J.iconsMap.set(e.name,o2.DOM.createHTML(e.svgStr)),null==document||document.querySelectorAll(`jp-icon[name="${e.name}"]`).forEach(t=>{t.setAttribute("name",""),t.setAttribute("name",e.name)})}static setDefaultIcon(e){J._defaultIcon=e}static defaultIcon(){return J._defaultIcon}nameChanged(){this.shadowRoot&&(this.shadowRoot.innerHTML=this.getSvg())}connectedCallback(){super.connectedCallback(),this.nameChanged()}getSvg(){var e;return null!=(e=J.iconsMap.get(this.name))?e:J.defaultIcon()}};rB.iconsMap=new Map,rB._defaultIcon=o2.DOM.createHTML(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16">
    <path
      d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"
      fill="currentColor"
    />
  </svg>`),re([o2.attr],rB.prototype,"name",void 0),rB=J=re([(0,o2.customElement)({name:"jp-icon",styles:rz})],rB);class rL extends K.Button{constructor(){super(...arguments),this.appearance="neutral"}defaultSlottedContentChanged(e,t){let o=this.defaultSlottedContent.filter(e=>e.nodeType===Node.ELEMENT_NODE);1===o.length&&(o[0]instanceof rB||o[0]instanceof SVGElement)?this.control.classList.add("icon-only"):this.control.classList.remove("icon-only")}}re([o2.attr],rL.prototype,"appearance",void 0),re([(0,o2.attr)({attribute:"minimal",mode:"boolean"})],rL.prototype,"minimal",void 0),re([o2.attr],rL.prototype,"scale",void 0);let rH=rL.compose({baseName:"button",baseClass:K.Button,template:K.buttonTemplate,styles:rj,shadowOptions:{delegatesFocus:!0}}),rN="box-shadow: 0 0 calc((var(--elevation) * 0.225px) + 2px) rgba(0, 0, 0, calc(.11 * (2 - var(--background-luminance, 1)))), 0 calc(var(--elevation) * 0.4px) calc((var(--elevation) * 0.9px)) rgba(0, 0, 0, calc(.13 * (2 - var(--background-luminance, 1))));",rO=(e,t)=>(0,o2.css)`
    ${(0,K.display)("block")} :host {
      --elevation: 4;
      display: block;
      contain: content;
      height: var(--card-height, 100%);
      width: var(--card-width, 100%);
      box-sizing: border-box;
      background: ${tz};
      border-radius: calc(${ek} * 1px);
      ${rN}
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        forced-color-adjust: none;
        background: ${Z.Canvas};
        box-shadow: 0 0 0 1px ${Z.CanvasText};
      }
    `));class rI extends K.Card{connectedCallback(){super.connectedCallback();let e=(0,K.composedParent)(this);e&&tz.setValueFor(this,t=>oc.getValueFor(t).evaluate(t,tz.getValueFor(e)))}}let rR=rI.compose({baseName:"card",baseClass:K.Card,template:K.cardTemplate,styles:rO}),rP=(e,t)=>(0,o2.css)`
    ${(0,K.display)("inline-flex")} :host {
      align-items: center;
      outline: none;
      margin: calc(${eC} * 1px) 0;
      /* Chromium likes to select label text or the default slot when the checkbox is
            clicked. Maybe there is a better solution here? */
      user-select: none;
    }

    .control {
      position: relative;
      width: calc((${o6} / 2 + ${eC}) * 1px);
      height: calc((${o6} / 2 + ${eC}) * 1px);
      box-sizing: border-box;
      border-radius: calc(${ek} * 1px);
      border: calc(${eT} * 1px) solid ${ox};
      background: ${t3};
      outline: none;
      cursor: pointer;
    }

    :host([aria-invalid='true']) .control {
      border-color: ${oj};
    }

    .label {
      font-family: ${e$};
      color: ${ov};
      /* Need to discuss with Brian how HorizontalSpacingNumber can work.
            https://github.com/microsoft/fast/issues/2766 */
      padding-inline-start: calc(${eC} * 2px + 2px);
      margin-inline-end: calc(${eC} * 2px + 2px);
      cursor: pointer;
      font-size: ${ez};
      line-height: ${eB};
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    .checked-indicator {
      width: 100%;
      height: 100%;
      display: block;
      fill: ${tP};
      opacity: 0;
      pointer-events: none;
    }

    .indeterminate-indicator {
      border-radius: calc(${ek} * 1px);
      background: ${tP};
      position: absolute;
      top: 50%;
      left: 50%;
      width: 50%;
      height: 50%;
      transform: translate(-50%, -50%);
      opacity: 0;
    }

    :host(:not([disabled])) .control:hover {
      background: ${t4};
      border-color: ${oy};
    }

    :host(:not([disabled])) .control:active {
      background: ${t9};
      border-color: ${ow};
    }

    :host([aria-invalid='true']:not([disabled])) .control:hover {
      border-color: ${oz};
    }

    :host([aria-invalid='true']:not([disabled])) .control:active {
      border-color: ${oB};
    }

    :host(:${K.focusVisible}) .control {
      outline: calc(${ej} * 1px) solid ${tO};
      outline-offset: 2px;
    }

    :host([aria-invalid='true']:${K.focusVisible}) .control {
      outline-color: ${oL};
    }

    :host([aria-checked='true']) .control {
      background: ${tL};
      border: calc(${eT} * 1px) solid ${tL};
    }

    :host([aria-checked='true']:not([disabled])) .control:hover {
      background: ${tH};
      border: calc(${eT} * 1px) solid ${tH};
    }

    :host([aria-invalid='true'][aria-checked='true']) .control {
      background-color: ${oj};
      border-color: ${oj};
    }

    :host([aria-invalid='true'][aria-checked='true']:not([disabled]))
      .control:hover {
      background-color: ${oz};
      border-color: ${oz};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:hover
      .checked-indicator {
      fill: ${tA};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:hover
      .indeterminate-indicator {
      background: ${tA};
    }

    :host([aria-checked='true']:not([disabled])) .control:active {
      background: ${tN};
      border: calc(${eT} * 1px) solid ${tN};
    }

    :host([aria-invalid='true'][aria-checked='true']:not([disabled]))
      .control:active {
      background-color: ${oB};
      border-color: ${oB};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:active
      .checked-indicator {
      fill: ${tM};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:active
      .indeterminate-indicator {
      background: ${tM};
    }

    :host([aria-checked="true"]:${K.focusVisible}:not([disabled])) .control {
      outline: calc(${ej} * 1px) solid ${tO};
      outline-offset: 2px;
    }

    :host([aria-invalid='true'][aria-checked="true"]:${K.focusVisible}:not([disabled])) .control {
      outline-color: ${oL};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
      cursor: ${K.disabledCursor};
    }

    :host([aria-checked='true']:not(.indeterminate)) .checked-indicator,
    :host(.indeterminate) .indeterminate-indicator {
      opacity: 1;
    }

    :host([disabled]) {
      opacity: ${eD};
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      .control {
        forced-color-adjust: none;
        border-color: ${Z.FieldText};
        background: ${Z.Field};
      }
      :host([aria-invalid='true']) .control {
        border-style: dashed;
      }
      .checked-indicator {
        fill: ${Z.FieldText};
      }
      .indeterminate-indicator {
        background: ${Z.FieldText};
      }
      :host(:not([disabled])) .control:hover,
      .control:active {
        border-color: ${Z.Highlight};
        background: ${Z.Field};
      }
      :host(:${K.focusVisible}) .control {
        outline: calc(${ej} * 1px) solid ${Z.FieldText};
        outline-offset: 2px;
      }
      :host([aria-checked="true"]:${K.focusVisible}:not([disabled])) .control {
        outline: calc(${ej} * 1px) solid ${Z.FieldText};
        outline-offset: 2px;
      }
      :host([aria-checked='true']) .control {
        background: ${Z.Highlight};
        border-color: ${Z.Highlight};
      }
      :host([aria-checked='true']:not([disabled])) .control:hover,
      .control:active {
        border-color: ${Z.Highlight};
        background: ${Z.HighlightText};
      }
      :host([aria-checked='true']) .checked-indicator {
        fill: ${Z.HighlightText};
      }
      :host([aria-checked='true']:not([disabled]))
        .control:hover
        .checked-indicator {
        fill: ${Z.Highlight};
      }
      :host([aria-checked='true']) .indeterminate-indicator {
        background: ${Z.HighlightText};
      }
      :host([aria-checked='true']) .control:hover .indeterminate-indicator {
        background: ${Z.Highlight};
      }
      :host([disabled]) {
        opacity: 1;
      }
      :host([disabled]) .control {
        forced-color-adjust: none;
        border-color: ${Z.GrayText};
        background: ${Z.Field};
      }
      :host([disabled]) .indeterminate-indicator,
      :host([aria-checked='true'][disabled])
        .control:hover
        .indeterminate-indicator {
        forced-color-adjust: none;
        background: ${Z.GrayText};
      }
      :host([disabled]) .checked-indicator,
      :host([aria-checked='true'][disabled]) .control:hover .checked-indicator {
        forced-color-adjust: none;
        fill: ${Z.GrayText};
      }
    `)),rA=(e,t)=>(0,o2.html)`
  <template
    role="checkbox"
    aria-checked="${e=>e.checked}"
    aria-required="${e=>e.required}"
    aria-disabled="${e=>e.disabled}"
    aria-readonly="${e=>e.readOnly}"
    tabindex="${e=>e.disabled?null:0}"
    @keypress="${(e,t)=>e.keypressHandler(t.event)}"
    @click="${(e,t)=>e.clickHandler(t.event)}"
  >
    <div part="control" class="control">
      <slot name="checked-indicator">
        ${t.checkedIndicator||""}
      </slot>
      <slot name="indeterminate-indicator">
        ${t.indeterminateIndicator||""}
      </slot>
    </div>
    <label
      part="label"
      class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
    >
      <slot ${(0,o2.slotted)("defaultSlottedNodes")}></slot>
    </label>
  </template>
`;class rM extends K.Checkbox{indeterminateChanged(e,t){this.indeterminate?this.classList.add("indeterminate"):this.classList.remove("indeterminate")}}let rG=rM.compose({baseName:"checkbox",baseClass:K.Checkbox,template:rA,styles:rP,checkedIndicator:`
        <svg
            part="checked-indicator"
            class="checked-indicator"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
        >
            <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M8.143 12.6697L15.235 4.5L16.8 5.90363L8.23812 15.7667L3.80005 11.2556L5.27591 9.7555L8.143 12.6697Z"
            />
        </svg>
    `,indeterminateIndicator:`
        <div part="indeterminate-indicator" class="indeterminate-indicator"></div>
    `}),rE=(e,t)=>{let o=e.tagFor(K.ListboxOption),r=e.name===e.tagFor(K.ListboxElement)?"":".listbox";return(0,o2.css)`
        ${!r?(0,K.display)("inline-flex"):""}

        :host ${r} {
            background: ${tz};
            border: calc(${eT} * 1px) solid ${ox};
            border-radius: calc(${ek} * 1px);
            box-sizing: border-box;
            flex-direction: column;
            padding: calc(${eC} * 1px) 0;
        }

        ${!r?(0,o2.css)`
:host(:${K.focusVisible}:not([disabled])) {
                outline: none;
            }

            :host(:focus-within:not([disabled])) {
                border-color: ${ou};
                box-shadow: 0 0 0
                    calc((${ej} - ${eT}) * 1px)
                    ${ou} inset;
            }

            :host([disabled]) ::slotted(*) {
                cursor: ${K.disabledCursor};
                opacity: ${eD};
                pointer-events: none;
            }
        `:""}

        ${r||":host([size])"} {
            max-height: calc(
                (var(--size) * ${o6} + (${eC} * ${eT} * 2)) * 1px
            );
            overflow-y: auto;
        }

        :host([size="0"]) ${r} {
            max-height: none;
        }
    `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
                :host(:not([multiple]):${K.focusVisible}) ::slotted(${o}[aria-selected="true"]),
                :host([multiple]:${K.focusVisible}) ::slotted(${o}[aria-checked="true"]) {
                    border-color: ${Z.ButtonText};
                    box-shadow: 0 0 0 calc(${ej} * 1px) inset ${Z.HighlightText};
                }

                :host(:not([multiple]):${K.focusVisible}) ::slotted(${o}[aria-selected="true"]) {
                    background: ${Z.Highlight};
                    color: ${Z.HighlightText};
                    fill: currentcolor;
                }

                ::slotted(${o}[aria-selected="true"]:not([aria-checked="true"])) {
                    background: ${Z.Highlight};
                    border-color: ${Z.HighlightText};
                    color: ${Z.HighlightText};
                }
            `))},r_=(e,t)=>{let o=e.name===e.tagFor(K.Select);return(0,o2.css)`
  ${(0,K.display)("inline-flex")}
  
  :host {
    --elevation: 14;
    background: ${t3};
    border-radius: calc(${ek} * 1px);
    border: calc(${eT} * 1px) solid ${oi};
    box-sizing: border-box;
    color: ${ov};
    font-family: ${e$};
    height: calc(${o6} * 1px);
    position: relative;
    user-select: none;
    min-width: 250px;
    outline: none;
    vertical-align: top;
  }

  :host([aria-invalid='true']) {
    border-color: ${oj};
  }
  
  :host(:not([autowidth])) {
    min-width: 250px;
  }
  
  ${o?(0,o2.css)`
  :host(:not([aria-haspopup])) {
    --elevation: 0;
    border: 0;
    height: auto;
    min-width: 0;
  }
  `:""}
  
  ${rE(e,t)}
  
  :host .listbox {
    ${rN}
    border: none;
    display: flex;
    left: 0;
    position: absolute;
    width: 100%;
    z-index: 1;
  }
  
  .control + .listbox {
    --stroke-size: calc(${eC} * ${eT} * 2);
    max-height: calc(
      (var(--listbox-max-height) * ${o6} + var(--stroke-size)) * 1px
      );
  }
  
  ${o?(0,o2.css)`
  :host(:not([aria-haspopup])) .listbox {
    left: auto;
    position: static;
    z-index: auto;
  }
  `:""}
  
  :host(:not([autowidth])) .listbox {
    width: 100%;
  }
  
  :host([autowidth]) ::slotted([role='option']),
  :host([autowidth]) ::slotted(option) {
    padding: 0 calc(1em + ${eC} * 1.25px + 1px);
  }
  
  .listbox[hidden] {
    display: none;
  }
  
  .control {
    align-items: center;
    box-sizing: border-box;
    cursor: pointer;
    display: flex;
    font-size: ${ez};
    font-family: inherit;
    line-height: ${eB};
    min-height: 100%;
    padding: 0 calc(${eC} * 2.25px);
    width: 100%;
  }

  :host([minimal]),
  :host([scale='xsmall']) {
    --element-scale: -4;
  }

  :host([scale='small']) {
    --element-scale: -2;
  }

  :host([scale='medium']) {
    --element-scale: 0;
  }

  :host([scale='large']) {
    --element-scale: 2;
  }

  :host([scale='xlarge']) {
    --element-scale: 4;
  }
  
  :host(:not([disabled]):hover) {
    background: ${t4};
    border-color: ${ol};
  }
  
  :host([aria-invalid='true']:not([disabled]):hover) {
    border-color: ${oz};
  }
  
  :host(:${K.focusVisible}) {
    border-color: ${tO};
    box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
    ${tO};
  }
  
  :host([aria-invalid='true']:${K.focusVisible}) {
    border-color: ${oL};
    box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
    ${oL};
  }
  
  :host(:not([size]):not([multiple]):not([open]):${K.focusVisible}),
  :host([multiple]:${K.focusVisible}),
  :host([size]:${K.focusVisible}) {
    box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
    ${tO};
  }
  
  :host([aria-invalid='true']:not([size]):not([multiple]):not([open]):${K.focusVisible}),
  :host([aria-invalid='true'][multiple]:${K.focusVisible}),
  :host([aria-invalid='true'][size]:${K.focusVisible}) {
    box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
    ${oL};
  }
  
  :host(:not([multiple]):not([size]):${K.focusVisible}) ::slotted(${e.tagFor(K.ListboxOption)}[aria-selected="true"]:not([disabled])) {
    box-shadow: 0 0 0 calc(${ej} * 1px) inset ${tO};
    border-color: ${tO};
    background: ${tO};
    color: ${tG};
  }
    
  :host([disabled]) {
    cursor: ${K.disabledCursor};
    opacity: ${eD};
  }
  
  :host([disabled]) .control {
    cursor: ${K.disabledCursor};
    user-select: none;
  }
  
  :host([disabled]:hover) {
    background: ${oe};
    color: ${ov};
    fill: currentcolor;
  }
  
  :host(:not([disabled])) .control:active {
    background: ${t9};
    border-color: ${tN};
    border-radius: calc(${ek} * 1px);
  }
  
  :host([open][position="above"]) .listbox {
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    border-bottom: 0;
    bottom: calc(${o6} * 1px);
  }
  
  :host([open][position="below"]) .listbox {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    border-top: 0;
    top: calc(${o6} * 1px);
  }
  
  .selected-value {
    flex: 1 1 auto;
    font-family: inherit;
    overflow: hidden;
    text-align: start;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  
  .indicator {
    flex: 0 0 auto;
    margin-inline-start: 1em;
  }
  
  slot[name="listbox"] {
    display: none;
    width: 100%;
  }
  
  :host([open]) slot[name="listbox"] {
    display: flex;
    position: absolute;
    ${rN}
  }
  
  .end {
    margin-inline-start: auto;
  }
  
  .start,
  .end,
  .indicator,
  .select-indicator,
  ::slotted(svg), 
  ::slotted(jp-icon) {
    /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
    fill: currentcolor;
    height: 1em;
    min-height: calc(${eC} * 4px);
    min-width: calc(${eC} * 4px);
    width: 1em;
  }
  
  ::slotted([role="option"]),
  ::slotted(option) {
    flex: 0 0 auto;
  }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host(:not([disabled]):hover),
      :host(:not([disabled]):active) {
        border-color: ${Z.Highlight};
      }

      :host([aria-invalid='true']) {
        border-style: dashed;
      }
      
      :host(:not([disabled]):${K.focusVisible}) {
        background-color: ${Z.ButtonFace};
        box-shadow: 0 0 0 calc(${ej} * 1px) ${Z.Highlight};
        color: ${Z.ButtonText};
        fill: currentcolor;
        forced-color-adjust: none;
      }
      
      :host(:not([disabled]):${K.focusVisible}) .listbox {
        background: ${Z.ButtonFace};
      }
      
      :host([disabled]) {
        border-color: ${Z.GrayText};
        background-color: ${Z.ButtonFace};
        color: ${Z.GrayText};
        fill: currentcolor;
        opacity: 1;
        forced-color-adjust: none;
      }
      
      :host([disabled]:hover) {
        background: ${Z.ButtonFace};
      }
      
      :host([disabled]) .control {
        color: ${Z.GrayText};
        border-color: ${Z.GrayText};
      }
      
      :host([disabled]) .control .select-indicator {
        fill: ${Z.GrayText};
      }
      
      :host(:${K.focusVisible}) ::slotted([aria-selected="true"][role="option"]),
      :host(:${K.focusVisible}) ::slotted(option[aria-selected="true"]),
      :host(:${K.focusVisible}) ::slotted([aria-selected="true"][role="option"]:not([disabled])) {
        background: ${Z.Highlight};
        border-color: ${Z.ButtonText};
        box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
        ${Z.HighlightText};
        color: ${Z.HighlightText};
        fill: currentcolor;
      }
      
      .start,
      .end,
      .indicator,
      .select-indicator,
      ::slotted(svg),
      ::slotted(jp-icon) {
        color: ${Z.ButtonText};
        fill: currentcolor;
      }
      `))},rq=(e,t)=>(0,o2.css)`
  ${r_(e,t)}

  :host(:empty) .listbox {
    display: none;
  }

  :host([disabled]) *,
  :host([disabled]) {
    cursor: ${K.disabledCursor};
    user-select: none;
  }

  :host(:focus-within:not([disabled])) {
    border-color: ${tO};
    box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
      ${tO};
  }

  :host([aria-invalid='true']:focus-within:not([disabled])) {
    border-color: ${oL};
    box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
      ${oL};
  }

  .selected-value {
    -webkit-appearance: none;
    background: transparent;
    border: none;
    color: inherit;
    font-size: ${ez};
    line-height: ${eB};
    height: calc(100% - (${eT} * 1px));
    margin: auto 0;
    width: 100%;
  }

  .selected-value:hover,
    .selected-value:${K.focusVisible},
    .selected-value:disabled,
    .selected-value:active {
    outline: none;
  }
`;class rW extends K.Combobox{connectedCallback(){super.connectedCallback(),this.setAutoWidth()}slottedOptionsChanged(e,t){super.slottedOptionsChanged(e,t),this.setAutoWidth()}autoWidthChanged(e,t){t?this.setAutoWidth():this.style.removeProperty("width")}setAutoWidth(){if(!this.autoWidth||!this.isConnected)return;let e=this.listbox.getBoundingClientRect().width;0===e&&this.listbox.hidden&&(Object.assign(this.listbox.style,{visibility:"hidden"}),this.listbox.removeAttribute("hidden"),e=this.listbox.getBoundingClientRect().width,this.listbox.setAttribute("hidden",""),this.listbox.style.removeProperty("visibility")),e>0&&Object.assign(this.style,{width:`${e}px`})}maxHeightChanged(e,t){this.updateComputedStylesheet()}updateComputedStylesheet(){this.computedStylesheet&&this.$fastController.removeStyles(this.computedStylesheet);let e=Math.floor(this.maxHeight/oS.getValueFor(this)).toString();this.computedStylesheet=(0,o2.css)`
      :host {
        --listbox-max-height: ${e};
      }
    `,this.$fastController.addStyles(this.computedStylesheet)}}re([(0,o2.attr)({attribute:"autowidth",mode:"boolean"})],rW.prototype,"autoWidth",void 0),re([(0,o2.attr)({attribute:"minimal",mode:"boolean"})],rW.prototype,"minimal",void 0),re([o2.attr],rW.prototype,"scale",void 0);let rU=rW.compose({baseName:"combobox",baseClass:K.Combobox,template:K.comboboxTemplate,styles:rq,shadowOptions:{delegatesFocus:!0},indicator:`
        <svg
            class="select-indicator"
            part="select-indicator"
            viewBox="0 0 12 7"
            xmlns="http://www.w3.org/2000/svg"
        >
            <path
                d="M11.85.65c.2.2.2.5 0 .7L6.4 6.84a.55.55 0 01-.78 0L.14 1.35a.5.5 0 11.71-.7L6 5.8 11.15.65c.2-.2.5-.2.7 0z"
            />
        </svg>
    `}),rX=(e,t)=>(0,o2.css)`
  :host {
    display: flex;
    position: relative;
    flex-direction: column;
  }
`,rY=(e,t)=>(0,o2.css)`
  :host {
    display: grid;
    padding: 1px 0;
    box-sizing: border-box;
    width: 100%;
    border-bottom: calc(${eT} * 1px) solid ${oC};
  }

  :host(.header) {
  }

  :host(.sticky-header) {
    background: ${t0};
    position: sticky;
    top: 0;
  }
`,rZ=(e,t)=>(0,o2.css)`
    :host {
      padding: calc(${eC} * 1px) calc(${eC} * 3px);
      color: ${ov};
      box-sizing: border-box;
      font-family: ${e$};
      font-size: ${ez};
      line-height: ${eB};
      font-weight: 400;
      border: transparent calc(${ej} * 1px) solid;
      overflow: hidden;
      white-space: nowrap;
      border-radius: calc(${ek} * 1px);
    }

    :host(.column-header) {
      font-weight: 600;
    }

    :host(:${K.focusVisible}) {
      outline: calc(${ej} * 1px) solid ${tO};
      color: ${ov};
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        forced-color-adjust: none;
        border-color: transparent;
        background: ${Z.Field};
        color: ${Z.FieldText};
      }

      :host(:${K.focusVisible}) {
        border-color: ${Z.FieldText};
        box-shadow: 0 0 0 2px inset ${Z.Field};
        color: ${Z.FieldText};
      }
    `));class rJ extends K.DataGridCell{}let rK=rJ.compose({baseName:"data-grid-cell",baseClass:K.DataGridCell,template:K.dataGridCellTemplate,styles:rZ});class rQ extends K.DataGridRow{}let r0=rQ.compose({baseName:"data-grid-row",baseClass:K.DataGridRow,template:K.dataGridRowTemplate,styles:rY});class r1 extends K.DataGrid{}let r2=r1.compose({baseName:"data-grid",baseClass:K.DataGrid,template:K.dataGridTemplate,styles:rX});var r5=o(59967);class r6 extends K.FoundationElement{}class r3 extends(0,K.FormAssociated)(r6){constructor(){super(...arguments),this.proxy=document.createElement("input")}}let r4={toView(e){if(null==e)return null;let t=new Date(e);return"Invalid Date"===t.toString()?null:`${t.getFullYear().toString().padStart(4,"0")}-${(t.getMonth()+1).toString().padStart(2,"0")}-${t.getDate().toString().padStart(2,"0")}`},fromView(e){if(null==e)return null;let t=new Date(e);return"Invalid Date"===t.toString()?null:t}},r9="Invalid Date";class r8 extends r3{constructor(){super(...arguments),this.step=1,this.isUserInput=!1}readOnlyChanged(){this.proxy instanceof HTMLInputElement&&(this.proxy.readOnly=this.readOnly,this.validate())}autofocusChanged(){this.proxy instanceof HTMLInputElement&&(this.proxy.autofocus=this.autofocus,this.validate())}listChanged(){this.proxy instanceof HTMLInputElement&&(this.proxy.setAttribute("list",this.list),this.validate())}maxChanged(e,t){var o;this.max=t<(null!=(o=this.min)?o:t)?this.min:t,this.value=this.getValidValue(this.value)}minChanged(e,t){var o;this.min=t>(null!=(o=this.max)?o:t)?this.max:t,this.value=this.getValidValue(this.value)}get valueAsNumber(){return new Date(super.value).valueOf()}set valueAsNumber(e){this.value=new Date(e).toString()}get valueAsDate(){return new Date(super.value)}set valueAsDate(e){this.value=e.toString()}valueChanged(e,t){this.value=this.getValidValue(t),t===this.value&&(this.control&&!this.isUserInput&&(this.control.value=this.value),super.valueChanged(e,this.value),void 0===e||this.isUserInput||this.$emit("change"),this.isUserInput=!1)}getValidValue(e){var t,o;let r=new Date(e);return r.toString()===r9?r="":(r=(r=r>(null!=(t=this.max)?t:r)?this.max:r)<(null!=(o=this.min)?o:r)?this.min:r,r=`${r.getFullYear().toString().padStart(4,"0")}-${(r.getMonth()+1).toString().padStart(2,"0")}-${r.getDate().toString().padStart(2,"0")}`),r}stepUp(){let e=864e5*this.step,t=new Date(this.value);this.value=new Date(t.toString()!==r9?t.valueOf()+e:0).toString()}stepDown(){let e=864e5*this.step,t=new Date(this.value);this.value=new Date(t.toString()!==r9?Math.max(t.valueOf()-e,0):0).toString()}connectedCallback(){super.connectedCallback(),this.validate(),this.control.value=this.value,this.autofocus&&o2.DOM.queueUpdate(()=>{this.focus()}),this.appearance||(this.appearance="outline")}handleTextInput(){this.isUserInput=!0,this.value=this.control.value}handleChange(){this.$emit("change")}handleKeyDown(e){switch(e.key){case r5.I5:return this.stepUp(),!1;case r5.HX:return this.stepDown(),!1}return!0}handleBlur(){this.control.value=this.value}}re([o2.attr],r8.prototype,"appearance",void 0),re([(0,o2.attr)({attribute:"readonly",mode:"boolean"})],r8.prototype,"readOnly",void 0),re([(0,o2.attr)({mode:"boolean"})],r8.prototype,"autofocus",void 0),re([o2.attr],r8.prototype,"list",void 0),re([(0,o2.attr)({converter:o2.nullableNumberConverter})],r8.prototype,"step",void 0),re([(0,o2.attr)({converter:r4})],r8.prototype,"max",void 0),re([(0,o2.attr)({converter:r4})],r8.prototype,"min",void 0),re([o2.observable],r8.prototype,"defaultSlottedNodes",void 0),(0,K.applyMixins)(r8,K.StartEnd,K.DelegatesARIATextbox);let r7=(0,o2.css)`
  ${(0,K.display)("inline-block")} :host {
    font-family: ${e$};
    outline: none;
    user-select: none;
    /* Ensure to display focus highlight */
    margin: calc((${ej} - ${eT}) * 1px);
  }

  .root {
    box-sizing: border-box;
    position: relative;
    display: flex;
    flex-direction: row;
    color: ${ov};
    background: ${t3};
    border-radius: calc(${ek} * 1px);
    border: calc(${eT} * 1px) solid ${oi};
    height: calc(${o6} * 1px);
  }

  :host([aria-invalid='true']) .root {
    border-color: ${oj};
  }

  .control {
    -webkit-appearance: none;
    font: inherit;
    background: transparent;
    border: 0;
    color: inherit;
    height: calc(100% - 4px);
    width: 100%;
    margin-top: auto;
    margin-bottom: auto;
    border: none;
    padding: 0 calc(${eC} * 2px + 1px);
    font-size: ${ez};
    line-height: ${eB};
  }

  .control:placeholder-shown {
    text-overflow: ellipsis;
  }

  .control:hover,
  .control:${K.focusVisible},
  .control:disabled,
  .control:active {
    outline: none;
  }

  .label {
    display: block;
    color: ${ov};
    cursor: pointer;
    font-size: ${ez};
    line-height: ${eB};
    margin-bottom: 4px;
  }

  .label__hidden {
    display: none;
    visibility: hidden;
  }

  .start,
  .end {
    margin: auto;
    fill: currentcolor;
  }

  ::slotted(svg),
  ::slotted(jp-icon) {
    /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
    width: 16px;
    height: 16px;
  }

  .start {
    margin-inline-start: 11px;
  }

  .end {
    margin-inline-end: 11px;
  }

  :host(:hover:not([disabled])) .root {
    background: ${t4};
    border-color: ${ol};
  }

  :host([aria-invalid='true']:hover:not([disabled])) .root {
    border-color: ${oz};
  }

  :host(:active:not([disabled])) .root {
    background: ${t4};
    border-color: ${os};
  }

  :host([aria-invalid='true']:active:not([disabled])) .root {
    border-color: ${oB};
  }

  :host(:focus-within:not([disabled])) .root {
    border-color: ${tO};
    box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
      ${tO};
  }

  :host([aria-invalid='true']:focus-within:not([disabled])) .root {
    border-color: ${oL};
    box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
      ${oL};
  }

  :host([appearance='filled']) .root {
    background: ${t0};
  }

  :host([appearance='filled']:hover:not([disabled])) .root {
    background: ${t1};
  }

  :host([disabled]) .label,
  :host([readonly]) .label,
  :host([readonly]) .control,
  :host([disabled]) .control {
    cursor: ${K.disabledCursor};
  }

  :host([disabled]) {
    opacity: ${eD};
  }

  :host([disabled]) .control {
    border-color: ${ox};
  }
`.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
    .root,
    :host([appearance='filled']) .root {
      forced-color-adjust: none;
      background: ${Z.Field};
      border-color: ${Z.FieldText};
    }
    :host([aria-invalid='true']) .root {
      border-style: dashed;
    }
    :host(:hover:not([disabled])) .root,
    :host([appearance='filled']:hover:not([disabled])) .root,
    :host([appearance='filled']:hover) .root {
      background: ${Z.Field};
      border-color: ${Z.Highlight};
    }
    .start,
    .end {
      fill: currentcolor;
    }
    :host([disabled]) {
      opacity: 1;
    }
    :host([disabled]) .root,
    :host([appearance='filled']:hover[disabled]) .root {
      border-color: ${Z.GrayText};
      background: ${Z.Field};
    }
    :host(:focus-within:enabled) .root {
      border-color: ${Z.Highlight};
      box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
        ${Z.Highlight};
    }
    input::placeholder {
      color: ${Z.GrayText};
    }
  `)),ae=(e,t)=>(0,o2.css)`
  ${r7}
`,at=(e,t)=>(0,o2.html)`
  <template class="${e=>e.readOnly?"readonly":""}">
    <label
      part="label"
      for="control"
      class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
    >
      <slot
        ${(0,o2.slotted)({property:"defaultSlottedNodes",filter:K.whitespaceFilter})}
      ></slot>
    </label>
    <div class="root" part="root">
      ${(0,K.startSlotTemplate)(e,t)}
      <input
        class="control"
        part="control"
        id="control"
        @input="${e=>e.handleTextInput()}"
        @change="${e=>e.handleChange()}"
        ?autofocus="${e=>e.autofocus}"
        ?disabled="${e=>e.disabled}"
        list="${e=>e.list}"
        ?readonly="${e=>e.readOnly}"
        ?required="${e=>e.required}"
        :value="${e=>e.value}"
        type="date"
        aria-atomic="${e=>e.ariaAtomic}"
        aria-busy="${e=>e.ariaBusy}"
        aria-controls="${e=>e.ariaControls}"
        aria-current="${e=>e.ariaCurrent}"
        aria-describedby="${e=>e.ariaDescribedby}"
        aria-details="${e=>e.ariaDetails}"
        aria-disabled="${e=>e.ariaDisabled}"
        aria-errormessage="${e=>e.ariaErrormessage}"
        aria-flowto="${e=>e.ariaFlowto}"
        aria-haspopup="${e=>e.ariaHaspopup}"
        aria-hidden="${e=>e.ariaHidden}"
        aria-invalid="${e=>e.ariaInvalid}"
        aria-keyshortcuts="${e=>e.ariaKeyshortcuts}"
        aria-label="${e=>e.ariaLabel}"
        aria-labelledby="${e=>e.ariaLabelledby}"
        aria-live="${e=>e.ariaLive}"
        aria-owns="${e=>e.ariaOwns}"
        aria-relevant="${e=>e.ariaRelevant}"
        aria-roledescription="${e=>e.ariaRoledescription}"
        ${(0,o2.ref)("control")}
      />
      ${(0,K.endSlotTemplate)(e,t)}
    </div>
  </template>
`,ao=r8.compose({baseName:"date-field",styles:ae,template:at,shadowOptions:{delegatesFocus:!0}}),ar={toView:e=>null==e?null:null==e?void 0:e.toColorString(),fromView(e){if(null==e)return null;let t=f(e);return t?I.create(t.r,t.g,t.b):null}},aa=(0,o2.css)`
  :host {
    background-color: ${tz};
    color: ${ov};
  }
`.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
    :host {
      background-color: ${Z.ButtonFace};
      box-shadow: 0 0 0 1px ${Z.CanvasText};
      color: ${Z.ButtonText};
    }
  `));function ai(e){return(t,o)=>{t[o+"Changed"]=function(t,o){null!=o?e.setValueFor(this,o):e.deleteValueFor(this)}}}class al extends K.FoundationElement{constructor(){super(),this.noPaint=!1;let e={handleChange:this.noPaintChanged.bind(this)};o2.Observable.getNotifier(this).subscribe(e,"fillColor"),o2.Observable.getNotifier(this).subscribe(e,"baseLayerLuminance")}noPaintChanged(){!this.noPaint&&(void 0!==this.fillColor||this.baseLayerLuminance)?this.$fastController.addStyles(aa):this.$fastController.removeStyles(aa)}}re([(0,o2.attr)({attribute:"no-paint",mode:"boolean"})],al.prototype,"noPaint",void 0),re([(0,o2.attr)({attribute:"fill-color",converter:ar}),ai(tz)],al.prototype,"fillColor",void 0),re([(0,o2.attr)({attribute:"accent-color",converter:ar,mode:"fromView"}),ai(tm)],al.prototype,"accentColor",void 0),re([(0,o2.attr)({attribute:"neutral-color",converter:ar,mode:"fromView"}),ai(tb)],al.prototype,"neutralColor",void 0),re([(0,o2.attr)({attribute:"error-color",converter:ar,mode:"fromView"}),ai(oV)],al.prototype,"errorColor",void 0),re([(0,o2.attr)({converter:o2.nullableNumberConverter}),ai(eF)],al.prototype,"density",void 0),re([(0,o2.attr)({attribute:"design-unit",converter:o2.nullableNumberConverter}),ai(eC)],al.prototype,"designUnit",void 0),re([(0,o2.attr)({attribute:"direction"}),ai(eV)],al.prototype,"direction",void 0),re([(0,o2.attr)({attribute:"base-height-multiplier",converter:o2.nullableNumberConverter}),ai(ex)],al.prototype,"baseHeightMultiplier",void 0),re([(0,o2.attr)({attribute:"base-horizontal-spacing-multiplier",converter:o2.nullableNumberConverter}),ai(ey)],al.prototype,"baseHorizontalSpacingMultiplier",void 0),re([(0,o2.attr)({attribute:"control-corner-radius",converter:o2.nullableNumberConverter}),ai(ek)],al.prototype,"controlCornerRadius",void 0),re([(0,o2.attr)({attribute:"stroke-width",converter:o2.nullableNumberConverter}),ai(eT)],al.prototype,"strokeWidth",void 0),re([(0,o2.attr)({attribute:"focus-stroke-width",converter:o2.nullableNumberConverter}),ai(ej)],al.prototype,"focusStrokeWidth",void 0),re([(0,o2.attr)({attribute:"disabled-opacity",converter:o2.nullableNumberConverter}),ai(eD)],al.prototype,"disabledOpacity",void 0),re([(0,o2.attr)({attribute:"type-ramp-minus-2-font-size"}),ai(eN)],al.prototype,"typeRampMinus2FontSize",void 0),re([(0,o2.attr)({attribute:"type-ramp-minus-2-line-height"}),ai(eO)],al.prototype,"typeRampMinus2LineHeight",void 0),re([(0,o2.attr)({attribute:"type-ramp-minus-1-font-size"}),ai(eL)],al.prototype,"typeRampMinus1FontSize",void 0),re([(0,o2.attr)({attribute:"type-ramp-minus-1-line-height"}),ai(eH)],al.prototype,"typeRampMinus1LineHeight",void 0),re([(0,o2.attr)({attribute:"type-ramp-base-font-size"}),ai(ez)],al.prototype,"typeRampBaseFontSize",void 0),re([(0,o2.attr)({attribute:"type-ramp-base-line-height"}),ai(eB)],al.prototype,"typeRampBaseLineHeight",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-1-font-size"}),ai(eI)],al.prototype,"typeRampPlus1FontSize",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-1-line-height"}),ai(eR)],al.prototype,"typeRampPlus1LineHeight",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-2-font-size"}),ai(eP)],al.prototype,"typeRampPlus2FontSize",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-2-line-height"}),ai(eA)],al.prototype,"typeRampPlus2LineHeight",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-3-font-size"}),ai(eM)],al.prototype,"typeRampPlus3FontSize",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-3-line-height"}),ai(eG)],al.prototype,"typeRampPlus3LineHeight",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-4-font-size"}),ai(eE)],al.prototype,"typeRampPlus4FontSize",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-4-line-height"}),ai(e_)],al.prototype,"typeRampPlus4LineHeight",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-5-font-size"}),ai(eq)],al.prototype,"typeRampPlus5FontSize",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-5-line-height"}),ai(eW)],al.prototype,"typeRampPlus5LineHeight",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-6-font-size"}),ai(eU)],al.prototype,"typeRampPlus6FontSize",void 0),re([(0,o2.attr)({attribute:"type-ramp-plus-6-line-height"}),ai(eX)],al.prototype,"typeRampPlus6LineHeight",void 0),re([(0,o2.attr)({attribute:"accent-fill-rest-delta",converter:o2.nullableNumberConverter}),ai(eY)],al.prototype,"accentFillRestDelta",void 0),re([(0,o2.attr)({attribute:"accent-fill-hover-delta",converter:o2.nullableNumberConverter}),ai(eZ)],al.prototype,"accentFillHoverDelta",void 0),re([(0,o2.attr)({attribute:"accent-fill-active-delta",converter:o2.nullableNumberConverter}),ai(eJ)],al.prototype,"accentFillActiveDelta",void 0),re([(0,o2.attr)({attribute:"accent-fill-focus-delta",converter:o2.nullableNumberConverter}),ai(eK)],al.prototype,"accentFillFocusDelta",void 0),re([(0,o2.attr)({attribute:"accent-foreground-rest-delta",converter:o2.nullableNumberConverter}),ai(eQ)],al.prototype,"accentForegroundRestDelta",void 0),re([(0,o2.attr)({attribute:"accent-foreground-hover-delta",converter:o2.nullableNumberConverter}),ai(e0)],al.prototype,"accentForegroundHoverDelta",void 0),re([(0,o2.attr)({attribute:"accent-foreground-active-delta",converter:o2.nullableNumberConverter}),ai(e1)],al.prototype,"accentForegroundActiveDelta",void 0),re([(0,o2.attr)({attribute:"accent-foreground-focus-delta",converter:o2.nullableNumberConverter}),ai(e2)],al.prototype,"accentForegroundFocusDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-rest-delta",converter:o2.nullableNumberConverter}),ai(e5)],al.prototype,"neutralFillRestDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-hover-delta",converter:o2.nullableNumberConverter}),ai(e6)],al.prototype,"neutralFillHoverDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-active-delta",converter:o2.nullableNumberConverter}),ai(e3)],al.prototype,"neutralFillActiveDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-focus-delta",converter:o2.nullableNumberConverter}),ai(e4)],al.prototype,"neutralFillFocusDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-input-rest-delta",converter:o2.nullableNumberConverter}),ai(e9)],al.prototype,"neutralFillInputRestDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-input-hover-delta",converter:o2.nullableNumberConverter}),ai(e8)],al.prototype,"neutralFillInputHoverDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-input-active-delta",converter:o2.nullableNumberConverter}),ai(e7)],al.prototype,"neutralFillInputActiveDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-input-focus-delta",converter:o2.nullableNumberConverter}),ai(te)],al.prototype,"neutralFillInputFocusDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-stealth-rest-delta",converter:o2.nullableNumberConverter}),ai(tt)],al.prototype,"neutralFillStealthRestDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-stealth-hover-delta",converter:o2.nullableNumberConverter}),ai(to)],al.prototype,"neutralFillStealthHoverDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-stealth-active-delta",converter:o2.nullableNumberConverter}),ai(tr)],al.prototype,"neutralFillStealthActiveDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-stealth-focus-delta",converter:o2.nullableNumberConverter}),ai(ta)],al.prototype,"neutralFillStealthFocusDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-strong-hover-delta",converter:o2.nullableNumberConverter}),ai(tl)],al.prototype,"neutralFillStrongHoverDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-strong-active-delta",converter:o2.nullableNumberConverter}),ai(ts)],al.prototype,"neutralFillStrongActiveDelta",void 0),re([(0,o2.attr)({attribute:"neutral-fill-strong-focus-delta",converter:o2.nullableNumberConverter}),ai(tn)],al.prototype,"neutralFillStrongFocusDelta",void 0),re([(0,o2.attr)({attribute:"base-layer-luminance",converter:o2.nullableNumberConverter}),ai(ew)],al.prototype,"baseLayerLuminance",void 0),re([(0,o2.attr)({attribute:"neutral-fill-layer-rest-delta",converter:o2.nullableNumberConverter}),ai(tc)],al.prototype,"neutralFillLayerRestDelta",void 0),re([(0,o2.attr)({attribute:"neutral-stroke-divider-rest-delta",converter:o2.nullableNumberConverter}),ai(tg)],al.prototype,"neutralStrokeDividerRestDelta",void 0),re([(0,o2.attr)({attribute:"neutral-stroke-rest-delta",converter:o2.nullableNumberConverter}),ai(td)],al.prototype,"neutralStrokeRestDelta",void 0),re([(0,o2.attr)({attribute:"neutral-stroke-hover-delta",converter:o2.nullableNumberConverter}),ai(th)],al.prototype,"neutralStrokeHoverDelta",void 0),re([(0,o2.attr)({attribute:"neutral-stroke-active-delta",converter:o2.nullableNumberConverter}),ai(tu)],al.prototype,"neutralStrokeActiveDelta",void 0),re([(0,o2.attr)({attribute:"neutral-stroke-focus-delta",converter:o2.nullableNumberConverter}),ai(tp)],al.prototype,"neutralStrokeFocusDelta",void 0);let as=(e,t)=>(0,o2.html)` <slot></slot> `,an=(e,t)=>(0,o2.css)`
  ${(0,K.display)("block")}
`,ac=al.compose({baseName:"design-system-provider",template:as,styles:an}),ad=(e,t)=>(0,o2.css)`
  :host([hidden]) {
    display: none;
  }

  :host {
    --elevation: 14;
    --dialog-height: 480px;
    --dialog-width: 640px;
    display: block;
  }

  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.3);
    touch-action: none;
  }

  .positioning-region {
    display: flex;
    justify-content: center;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    overflow: auto;
  }

  .control {
    ${rN}
    margin-top: auto;
    margin-bottom: auto;
    width: var(--dialog-width);
    height: var(--dialog-height);
    background-color: ${tz};
    z-index: 1;
    border-radius: calc(${ek} * 1px);
    border: calc(${eT} * 1px) solid transparent;
  }
`;class ah extends K.Dialog{}let au=ah.compose({baseName:"dialog",baseClass:K.Dialog,template:K.dialogTemplate,styles:ad}),ap=(e,t)=>(0,o2.css)`
  .disclosure {
    transition: height 0.35s;
  }

  .disclosure .invoker::-webkit-details-marker {
    display: none;
  }

  .disclosure .invoker {
    list-style-type: none;
  }

  :host([appearance='accent']) .invoker {
    background: ${tL};
    color: ${tP};
    font-family: ${e$};
    font-size: ${ez};
    border-radius: calc(${ek} * 1px);
    outline: none;
    cursor: pointer;
    margin: 16px 0;
    padding: 12px;
    max-width: max-content;
  }

  :host([appearance='accent']) .invoker:active {
    background: ${tN};
    color: ${tM};
  }

  :host([appearance='accent']) .invoker:hover {
    background: ${tH};
    color: ${tA};
  }

  :host([appearance='lightweight']) .invoker {
    background: transparent;
    color: ${tY};
    border-bottom: calc(${eT} * 1px) solid ${tY};
    cursor: pointer;
    width: max-content;
    margin: 16px 0;
  }

  :host([appearance='lightweight']) .invoker:active {
    border-bottom-color: ${tJ};
  }

  :host([appearance='lightweight']) .invoker:hover {
    border-bottom-color: ${tZ};
  }

  .disclosure[open] .invoker ~ * {
    animation: fadeIn 0.5s ease-in-out;
  }

  @keyframes fadeIn {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }
`;class ag extends K.Disclosure{constructor(){super(...arguments),this.height=0,this.totalHeight=0}connectedCallback(){super.connectedCallback(),this.appearance||(this.appearance="accent")}appearanceChanged(e,t){e!==t&&(this.classList.add(t),this.classList.remove(e))}onToggle(){super.onToggle(),this.details.style.setProperty("height",`${this.disclosureHeight}px`)}setup(){super.setup();let e=()=>this.details.getBoundingClientRect().height;this.show(),this.totalHeight=e(),this.hide(),this.height=e(),this.expanded&&this.show()}get disclosureHeight(){return this.expanded?this.totalHeight:this.height}}re([o2.attr],ag.prototype,"appearance",void 0);let ab=ag.compose({baseName:"disclosure",baseClass:K.Disclosure,template:K.disclosureTemplate,styles:ap}),af=(e,t)=>(0,o2.css)`
  ${(0,K.display)("block")} :host {
    box-sizing: content-box;
    height: 0;
    margin: calc(${eC} * 1px) 0;
    border-top: calc(${eT} * 1px) solid ${oC};
    border-left: none;
  }

  :host([orientation='vertical']) {
    height: 100%;
    margin: 0 calc(${eC} * 1px);
    border-top: none;
    border-left: calc(${eT} * 1px) solid ${oC};
  }
`;class am extends K.Divider{}let av=am.compose({baseName:"divider",baseClass:K.Divider,template:K.dividerTemplate,styles:af});class a$ extends K.ListboxElement{sizeChanged(e,t){super.sizeChanged(e,t),this.updateComputedStylesheet()}updateComputedStylesheet(){this.computedStylesheet&&this.$fastController.removeStyles(this.computedStylesheet);let e=`${this.size}`;this.computedStylesheet=(0,o2.css)`
      :host {
        --size: ${e};
      }
    `,this.$fastController.addStyles(this.computedStylesheet)}}let ax=a$.compose({baseName:"listbox",baseClass:K.ListboxElement,template:K.listboxTemplate,styles:rE}),ay=(e,t)=>(0,o2.css)`
    ${(0,K.display)("block")} :host {
      --elevation: 11;
      background: ${tz};
      border: calc(${eT} * 1px) solid transparent;
      ${rN}
      margin: 0;
      border-radius: calc(${ek} * 1px);
      padding: calc(${eC} * 1px) 0;
      max-width: 368px;
      min-width: 64px;
    }

    :host([slot='submenu']) {
      width: max-content;
      margin: 0 calc(${eC} * 1px);
    }

    ::slotted(hr) {
      box-sizing: content-box;
      height: 0;
      margin: 0;
      border: none;
      border-top: calc(${eT} * 1px) solid ${oC};
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        background: ${Z.Canvas};
        border-color: ${Z.CanvasText};
      }
    `));class aw extends K.Menu{connectedCallback(){super.connectedCallback(),tz.setValueFor(this,tw)}}let ak=aw.compose({baseName:"menu",baseClass:K.Menu,template:K.menuTemplate,styles:ay}),aF=(e,t)=>(0,o2.css)`
    ${(0,K.display)("grid")} :host {
      contain: layout;
      overflow: visible;
      font-family: ${e$};
      outline: none;
      box-sizing: border-box;
      height: calc(${o6} * 1px);
      grid-template-columns: minmax(42px, auto) 1fr minmax(42px, auto);
      grid-template-rows: auto;
      justify-items: center;
      align-items: center;
      padding: 0;
      margin: 0 calc(${eC} * 1px);
      white-space: nowrap;
      background: ${oe};
      color: ${ov};
      fill: currentcolor;
      cursor: pointer;
      font-size: ${ez};
      line-height: ${eB};
      border-radius: calc(${ek} * 1px);
      border: calc(${ej} * 1px) solid transparent;
    }

    :host(:hover) {
      position: relative;
      z-index: 1;
    }

    :host(.indent-0) {
      grid-template-columns: auto 1fr minmax(42px, auto);
    }
    :host(.indent-0) .content {
      grid-column: 1;
      grid-row: 1;
      margin-inline-start: 10px;
    }
    :host(.indent-0) .expand-collapse-glyph-container {
      grid-column: 5;
      grid-row: 1;
    }
    :host(.indent-2) {
      grid-template-columns:
        minmax(42px, auto) minmax(42px, auto) 1fr minmax(42px, auto)
        minmax(42px, auto);
    }
    :host(.indent-2) .content {
      grid-column: 3;
      grid-row: 1;
      margin-inline-start: 10px;
    }
    :host(.indent-2) .expand-collapse-glyph-container {
      grid-column: 5;
      grid-row: 1;
    }
    :host(.indent-2) .start {
      grid-column: 2;
    }
    :host(.indent-2) .end {
      grid-column: 4;
    }

    :host(:${K.focusVisible}) {
      border-color: ${tO};
      background: ${or};
      color: ${ov};
    }

    :host(:hover) {
      background: ${ot};
      color: ${ov};
    }

    :host(:active) {
      background: ${oo};
    }

    :host([aria-checked='true']),
    :host(.expanded) {
      background: ${t0};
      color: ${ov};
    }

    :host([disabled]) {
      cursor: ${K.disabledCursor};
      opacity: ${eD};
    }

    :host([disabled]:hover) {
      color: ${ov};
      fill: currentcolor;
      background: ${oe};
    }

    :host([disabled]:hover) .start,
    :host([disabled]:hover) .end,
    :host([disabled]:hover)::slotted(svg),
    :host([disabled]:hover)::slotted(jp-icon) {
      fill: ${ov};
    }

    .expand-collapse-glyph {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: calc((16 + ${eF}) * 1px);
      height: calc((16 + ${eF}) * 1px);
      fill: currentcolor;
    }

    .content {
      grid-column-start: 2;
      justify-self: start;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .start,
    .end {
      display: flex;
      justify-content: center;
    }

    ::slotted(svg),
    ::slotted(jp-icon) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;

      /* Something like that would do if the typography is adaptive
      font-size: inherit;
      width: ${eI};
      height: ${eI};
      */
    }

    :host(:hover) .start,
    :host(:hover) .end,
    :host(:hover)::slotted(svg),
    :host(:hover)::slotted(jp-icon),
    :host(:active) .start,
    :host(:active) .end,
    :host(:active)::slotted(svg),
    :host(:active)::slotted(jp-icon) {
      fill: ${ov};
    }

    :host(.indent-0[aria-haspopup='menu']) {
      display: grid;
      grid-template-columns: minmax(42px, auto) auto 1fr minmax(42px, auto) minmax(
          42px,
          auto
        );
      align-items: center;
      min-height: 32px;
    }

    :host(.indent-1[aria-haspopup='menu']),
    :host(.indent-1[role='menuitemcheckbox']),
    :host(.indent-1[role='menuitemradio']) {
      display: grid;
      grid-template-columns: minmax(42px, auto) auto 1fr minmax(42px, auto) minmax(
          42px,
          auto
        );
      align-items: center;
      min-height: 32px;
    }

    :host(.indent-2:not([aria-haspopup='menu'])) .end {
      grid-column: 5;
    }

    :host .input-container,
    :host .expand-collapse-glyph-container {
      display: none;
    }

    :host([aria-haspopup='menu']) .expand-collapse-glyph-container,
    :host([role='menuitemcheckbox']) .input-container,
    :host([role='menuitemradio']) .input-container {
      display: grid;
      margin-inline-end: 10px;
    }

    :host([aria-haspopup='menu']) .content,
    :host([role='menuitemcheckbox']) .content,
    :host([role='menuitemradio']) .content {
      grid-column-start: 3;
    }

    :host([aria-haspopup='menu'].indent-0) .content {
      grid-column-start: 1;
    }

    :host([aria-haspopup='menu']) .end,
    :host([role='menuitemcheckbox']) .end,
    :host([role='menuitemradio']) .end {
      grid-column-start: 4;
    }

    :host .expand-collapse,
    :host .checkbox,
    :host .radio {
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      width: 20px;
      height: 20px;
      box-sizing: border-box;
      outline: none;
      margin-inline-start: 10px;
    }

    :host .checkbox,
    :host .radio {
      border: calc(${eT} * 1px) solid ${ov};
    }

    :host([aria-checked='true']) .checkbox,
    :host([aria-checked='true']) .radio {
      background: ${tL};
      border-color: ${tL};
    }

    :host .checkbox {
      border-radius: calc(${ek} * 1px);
    }

    :host .radio {
      border-radius: 999px;
    }

    :host .checkbox-indicator,
    :host .radio-indicator,
    :host .expand-collapse-indicator,
    ::slotted([slot='checkbox-indicator']),
    ::slotted([slot='radio-indicator']),
    ::slotted([slot='expand-collapse-indicator']) {
      display: none;
    }

    ::slotted([slot='end']:not(svg)) {
      margin-inline-end: 10px;
      color: ${of};
    }

    :host([aria-checked='true']) .checkbox-indicator,
    :host([aria-checked='true']) ::slotted([slot='checkbox-indicator']) {
      width: 100%;
      height: 100%;
      display: block;
      fill: ${tP};
      pointer-events: none;
    }

    :host([aria-checked='true']) .radio-indicator {
      position: absolute;
      top: 4px;
      left: 4px;
      right: 4px;
      bottom: 4px;
      border-radius: 999px;
      display: block;
      background: ${tP};
      pointer-events: none;
    }

    :host([aria-checked='true']) ::slotted([slot='radio-indicator']) {
      display: block;
      pointer-events: none;
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        border-color: transparent;
        color: ${Z.ButtonText};
        forced-color-adjust: none;
      }

      :host(:hover) {
        background: ${Z.Highlight};
        color: ${Z.HighlightText};
      }

      :host(:hover) .start,
      :host(:hover) .end,
      :host(:hover)::slotted(svg),
      :host(:hover)::slotted(jp-icon),
      :host(:active) .start,
      :host(:active) .end,
      :host(:active)::slotted(svg),
      :host(:active)::slotted(jp-icon) {
        fill: ${Z.HighlightText};
      }

      :host(.expanded) {
        background: ${Z.Highlight};
        border-color: ${Z.Highlight};
        color: ${Z.HighlightText};
      }

      :host(:${K.focusVisible}) {
        background: ${Z.Highlight};
        border-color: ${Z.ButtonText};
        box-shadow: 0 0 0 calc(${ej} * 1px) inset
          ${Z.HighlightText};
        color: ${Z.HighlightText};
        fill: currentcolor;
      }

      :host([disabled]),
      :host([disabled]:hover),
      :host([disabled]:hover) .start,
      :host([disabled]:hover) .end,
      :host([disabled]:hover)::slotted(svg),
      :host([disabled]:hover)::slotted(jp-icon) {
        background: ${Z.Canvas};
        color: ${Z.GrayText};
        fill: currentcolor;
        opacity: 1;
      }

      :host .expanded-toggle,
      :host .checkbox,
      :host .radio {
        border-color: ${Z.ButtonText};
        background: ${Z.HighlightText};
      }

      :host([checked='true']) .checkbox,
      :host([checked='true']) .radio {
        background: ${Z.HighlightText};
        border-color: ${Z.HighlightText};
      }

      :host(:hover) .expanded-toggle,
            :host(:hover) .checkbox,
            :host(:hover) .radio,
            :host(:${K.focusVisible}) .expanded-toggle,
            :host(:${K.focusVisible}) .checkbox,
            :host(:${K.focusVisible}) .radio,
            :host([checked="true"]:hover) .checkbox,
            :host([checked="true"]:hover) .radio,
            :host([checked="true"]:${K.focusVisible}) .checkbox,
            :host([checked="true"]:${K.focusVisible}) .radio {
        border-color: ${Z.HighlightText};
      }

      :host([aria-checked='true']) {
        background: ${Z.Highlight};
        color: ${Z.HighlightText};
      }

      :host([aria-checked='true']) .checkbox-indicator,
      :host([aria-checked='true']) ::slotted([slot='checkbox-indicator']),
      :host([aria-checked='true']) ::slotted([slot='radio-indicator']) {
        fill: ${Z.Highlight};
      }

      :host([aria-checked='true']) .radio-indicator {
        background: ${Z.Highlight};
      }

      ::slotted([slot='end']:not(svg)) {
        color: ${Z.ButtonText};
      }

      :host(:hover) ::slotted([slot="end"]:not(svg)),
            :host(:${K.focusVisible}) ::slotted([slot="end"]:not(svg)) {
        color: ${Z.HighlightText};
      }
    `),new rb((0,o2.css)`
        .expand-collapse-glyph {
          transform: rotate(0deg);
        }
      `,(0,o2.css)`
        .expand-collapse-glyph {
          transform: rotate(180deg);
        }
      `));class aC extends K.MenuItem{}let aS=aC.compose({baseName:"menu-item",baseClass:K.MenuItem,template:K.menuItemTemplate,styles:aF,checkboxIndicator:`
        <svg
            part="checkbox-indicator"
            class="checkbox-indicator"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
        >
            <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M8.143 12.6697L15.235 4.5L16.8 5.90363L8.23812 15.7667L3.80005 11.2556L5.27591 9.7555L8.143 12.6697Z"
            />
        </svg>
    `,expandCollapseGlyph:`
        <svg
            viewBox="0 0 16 16"
            xmlns="http://www.w3.org/2000/svg"
            class="expand-collapse-glyph"
            part="expand-collapse-glyph"
        >
            <path
                d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"
            />
        </svg>
    `,radioIndicator:`
        <span part="radio-indicator" class="radio-indicator"></span>
    `}),aV=(e,t)=>(0,o2.css)`
  ${r7}

  .controls {
    opacity: 0;
    margin: auto 0;
  }

  .step-up-glyph,
  .step-down-glyph {
    display: block;
    padding: calc(
        (${eC} + 0.5 * ${eF} + 0.5 * ${eS}) * 1px
      )
      calc((2 + 2 * ${eC} + ${eF} + ${eS}) * 1px);
    cursor: pointer;
  }

  .step-up-glyph:before,
  .step-down-glyph:before {
    content: '';
    display: block;
    border: solid transparent
      calc((2 + ${eC} + 0.5 * ${eF} + 0.5 * ${eS}) * 1px);
  }

  .step-up-glyph:hover:before,
  .step-down-glyph:hover:before {
    background-color: ${t1};
  }

  .step-up-glyph:active:before,
  .step-down-glyph:active:before {
    background-color: ${t2};
  }

  .step-up-glyph:before {
    border-bottom-color: ${ov};
  }

  .step-down-glyph:before {
    border-top-color: ${ov};
  }

  :host(:hover:not([disabled])) .controls,
  :host(:focus-within:not([disabled])) .controls {
    opacity: 1;
  }
`;class aD extends K.NumberField{constructor(){super(...arguments),this.appearance="outline"}}re([o2.attr],aD.prototype,"appearance",void 0);let aT=aD.compose({baseName:"number-field",baseClass:K.NumberField,styles:aV,template:K.numberFieldTemplate,shadowOptions:{delegatesFocus:!0},stepDownGlyph:`
        <span class="step-down-glyph" part="step-down-glyph"></span>
    `,stepUpGlyph:`
        <span class="step-up-glyph" part="step-up-glyph"></span>
    `}),aj=(e,t)=>(0,o2.css)`
    ${(0,K.display)("inline-flex")} :host {
      align-items: center;
      font-family: ${e$};
      border-radius: calc(${ek} * 1px);
      border: calc(${ej} * 1px) solid transparent;
      box-sizing: border-box;
      background: ${oe};
      color: ${ov};
      cursor: pointer;
      flex: 0 0 auto;
      fill: currentcolor;
      font-size: ${ez};
      height: calc(${o6} * 1px);
      line-height: ${eB};
      margin: 0 calc((${eC} - ${ej}) * 1px);
      outline: none;
      overflow: hidden;
      padding: 0 1ch;
      user-select: none;
      white-space: nowrap;
    }

    :host(:not([disabled]):not([aria-selected='true']):hover) {
      background: ${ot};
    }

    :host(:not([disabled]):not([aria-selected='true']):active) {
      background: ${oo};
    }

    :host([aria-selected='true']) {
      background: ${tL};
      color: ${tP};
    }

    :host(:not([disabled])[aria-selected='true']:hover) {
      background: ${tH};
      color: ${tA};
    }

    :host(:not([disabled])[aria-selected='true']:active) {
      background: ${tN};
      color: ${tM};
    }

    :host([disabled]) {
      cursor: ${K.disabledCursor};
      opacity: ${eD};
    }

    .content {
      grid-column-start: 2;
      justify-self: start;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .start,
    .end,
    ::slotted(svg),
    ::slotted(jp-icon) {
      display: flex;
    }

    ::slotted(svg),
    ::slotted(jp-icon) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      height: calc(${eC} * 4px);
      width: calc(${eC} * 4px);
    }

    ::slotted([slot='end']) {
      margin-inline-start: 1ch;
    }

    ::slotted([slot='start']) {
      margin-inline-end: 1ch;
    }

    :host([aria-checked='true'][aria-selected='false']) {
      border-color: ${ou};
    }

    :host([aria-checked='true'][aria-selected='true']) {
      border-color: ${ou};
      box-shadow: 0 0 0 calc(${ej} * 2 * 1px) inset
        ${og};
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        border-color: transparent;
        forced-color-adjust: none;
        color: ${Z.ButtonText};
        fill: currentcolor;
      }

      :host(:not([aria-selected='true']):hover),
      :host([aria-selected='true']) {
        background: ${Z.Highlight};
        color: ${Z.HighlightText};
      }

      :host([disabled]),
      :host([disabled][aria-selected='false']:hover) {
        background: ${Z.Canvas};
        color: ${Z.GrayText};
        fill: currentcolor;
        opacity: 1;
      }

      :host([aria-checked='true'][aria-selected='false']) {
        background: ${Z.ButtonFace};
        color: ${Z.ButtonText};
        border-color: ${Z.ButtonText};
      }

      :host([aria-checked='true'][aria-selected='true']),
      :host([aria-checked='true'][aria-selected='true']:hover) {
        background: ${Z.Highlight};
        color: ${Z.HighlightText};
        border-color: ${Z.ButtonText};
      }
    `));class az extends K.ListboxOption{}let aB=az.compose({baseName:"option",baseClass:K.ListboxOption,template:K.listboxOptionTemplate,styles:aj}),aL=(e,t)=>(0,o2.css)`
    ${(0,K.display)("flex")} :host {
      align-items: center;
      outline: none;
      height: calc(${eC} * 1px);
      margin: calc(${eC} * 1px) 0;
    }

    .progress {
      background-color: ${t0};
      border-radius: calc(${eC} * 1px);
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      position: relative;
    }

    .determinate {
      background-color: ${tY};
      border-radius: calc(${eC} * 1px);
      height: 100%;
      transition: all 0.2s ease-in-out;
      display: flex;
    }

    .indeterminate {
      height: 100%;
      border-radius: calc(${eC} * 1px);
      display: flex;
      width: 100%;
      position: relative;
      overflow: hidden;
    }

    .indeterminate-indicator-1 {
      position: absolute;
      opacity: 0;
      height: 100%;
      background-color: ${tY};
      border-radius: calc(${eC} * 1px);
      animation-timing-function: cubic-bezier(0.4, 0, 0.6, 1);
      width: 40%;
      animation: indeterminate-1 2s infinite;
    }

    .indeterminate-indicator-2 {
      position: absolute;
      opacity: 0;
      height: 100%;
      background-color: ${tY};
      border-radius: calc(${eC} * 1px);
      animation-timing-function: cubic-bezier(0.4, 0, 0.6, 1);
      width: 60%;
      animation: indeterminate-2 2s infinite;
    }

    :host([paused]) .indeterminate-indicator-1,
    :host([paused]) .indeterminate-indicator-2 {
      animation-play-state: paused;
      background-color: ${t0};
    }

    :host([paused]) .determinate {
      background-color: ${of};
    }

    @keyframes indeterminate-1 {
      0% {
        opacity: 1;
        transform: translateX(-100%);
      }
      70% {
        opacity: 1;
        transform: translateX(300%);
      }
      70.01% {
        opacity: 0;
      }
      100% {
        opacity: 0;
        transform: translateX(300%);
      }
    }

    @keyframes indeterminate-2 {
      0% {
        opacity: 0;
        transform: translateX(-150%);
      }
      29.99% {
        opacity: 0;
      }
      30% {
        opacity: 1;
        transform: translateX(-150%);
      }
      100% {
        transform: translateX(166.66%);
        opacity: 1;
      }
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      .progress {
        forced-color-adjust: none;
        background-color: ${Z.Field};
        box-shadow: 0 0 0 1px inset ${Z.FieldText};
      }
      .determinate,
      .indeterminate-indicator-1,
      .indeterminate-indicator-2 {
        forced-color-adjust: none;
        background-color: ${Z.FieldText};
      }
      :host([paused]) .determinate,
      :host([paused]) .indeterminate-indicator-1,
      :host([paused]) .indeterminate-indicator-2 {
        background-color: ${Z.GrayText};
      }
    `));class aH extends K.BaseProgress{}let aN=aH.compose({baseName:"progress",baseClass:K.BaseProgress,template:K.progressTemplate,styles:aL,indeterminateIndicator1:`
        <span class="indeterminate-indicator-1" part="indeterminate-indicator-1"></span>
    `,indeterminateIndicator2:`
        <span class="indeterminate-indicator-2" part="indeterminate-indicator-2"></span>
    `}),aO=(e,t)=>(0,o2.css)`
    ${(0,K.display)("flex")} :host {
      align-items: center;
      outline: none;
      height: calc(${o6} * 1px);
      width: calc(${o6} * 1px);
      margin: calc(${o6} * 1px) 0;
    }

    .progress {
      height: 100%;
      width: 100%;
    }

    .background {
      stroke: ${t0};
      fill: none;
      stroke-width: 2px;
    }

    .determinate {
      stroke: ${tY};
      fill: none;
      stroke-width: 2px;
      stroke-linecap: round;
      transform-origin: 50% 50%;
      transform: rotate(-90deg);
      transition: all 0.2s ease-in-out;
    }

    .indeterminate-indicator-1 {
      stroke: ${tY};
      fill: none;
      stroke-width: 2px;
      stroke-linecap: round;
      transform-origin: 50% 50%;
      transform: rotate(-90deg);
      transition: all 0.2s ease-in-out;
      animation: spin-infinite 2s linear infinite;
    }

    :host([paused]) .indeterminate-indicator-1 {
      animation-play-state: paused;
      stroke: ${t0};
    }

    :host([paused]) .determinate {
      stroke: ${of};
    }

    @keyframes spin-infinite {
      0% {
        stroke-dasharray: 0.01px 43.97px;
        transform: rotate(0deg);
      }
      50% {
        stroke-dasharray: 21.99px 21.99px;
        transform: rotate(450deg);
      }
      100% {
        stroke-dasharray: 0.01px 43.97px;
        transform: rotate(1080deg);
      }
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      .indeterminate-indicator-1,
      .determinate {
        stroke: ${Z.FieldText};
      }
      .background {
        stroke: ${Z.Field};
      }
      :host([paused]) .indeterminate-indicator-1 {
        stroke: ${Z.Field};
      }
      :host([paused]) .determinate {
        stroke: ${Z.GrayText};
      }
    `));class aI extends K.BaseProgress{}let aR=aI.compose({baseName:"progress-ring",baseClass:K.BaseProgress,template:K.progressRingTemplate,styles:aO,indeterminateIndicator:`
        <svg class="progress" part="progress" viewBox="0 0 16 16">
            <circle
                class="background"
                part="background"
                cx="8px"
                cy="8px"
                r="7px"
            ></circle>
            <circle
                class="indeterminate-indicator-1"
                part="indeterminate-indicator-1"
                cx="8px"
                cy="8px"
                r="7px"
            ></circle>
        </svg>
    `}),aP=(e,t)=>(0,o2.css)`
    ${(0,K.display)("inline-flex")} :host {
      --input-size: calc((${o6} / 2) + ${eC});
      align-items: center;
      outline: none;
      margin: calc(${eC} * 1px) 0;
      /* Chromium likes to select label text or the default slot when
                the radio is clicked. Maybe there is a better solution here? */
      user-select: none;
      position: relative;
      flex-direction: row;
      transition: all 0.2s ease-in-out;
    }

    .control {
      position: relative;
      width: calc((${o6} / 2 + ${eC}) * 1px);
      height: calc((${o6} / 2 + ${eC}) * 1px);
      box-sizing: border-box;
      border-radius: 999px;
      border: calc(${eT} * 1px) solid ${ox};
      background: ${t3};
      outline: none;
      cursor: pointer;
    }

    :host([aria-invalid='true']) .control {
      border-color: ${oj};
    }

    .label {
      font-family: ${e$};
      color: ${ov};
      padding-inline-start: calc(${eC} * 2px + 2px);
      margin-inline-end: calc(${eC} * 2px + 2px);
      cursor: pointer;
      font-size: ${ez};
      line-height: ${eB};
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    .control,
    .checked-indicator {
      flex-shrink: 0;
    }

    .checked-indicator {
      position: absolute;
      top: 5px;
      left: 5px;
      right: 5px;
      bottom: 5px;
      border-radius: 999px;
      display: inline-block;
      background: ${tP};
      fill: ${tP};
      opacity: 0;
      pointer-events: none;
    }

    :host(:not([disabled])) .control:hover {
      background: ${t4};
      border-color: ${oy};
    }

    :host([aria-invalid='true']:not([disabled])) .control:hover {
      border-color: ${oz};
    }

    :host(:not([disabled])) .control:active {
      background: ${t9};
      border-color: ${ow};
    }

    :host([aria-invalid='true']:not([disabled])) .control:active {
      border-color: ${oB};
    }

    :host(:${K.focusVisible}) .control {
      outline: solid calc(${ej} * 1px) ${tO};
    }

    :host([aria-invalid='true']:${K.focusVisible}) .control {
      outline-color: ${oL};
    }

    :host([aria-checked='true']) .control {
      background: ${tL};
      border: calc(${eT} * 1px) solid ${tL};
    }

    :host([aria-invalid='true'][aria-checked='true']) .control {
      background-color: ${oj};
      border-color: ${oj};
    }

    :host([aria-checked='true']:not([disabled])) .control:hover {
      background: ${tH};
      border: calc(${eT} * 1px) solid ${tH};
    }

    :host([aria-invalid='true'][aria-checked='true']:not([disabled]))
      .control:hover {
      background-color: ${oz};
      border-color: ${oz};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:hover
      .checked-indicator {
      background: ${tA};
      fill: ${tA};
    }

    :host([aria-checked='true']:not([disabled])) .control:active {
      background: ${tN};
      border: calc(${eT} * 1px) solid ${tN};
    }

    :host([aria-invalid='true'][aria-checked='true']:not([disabled]))
      .control:active {
      background-color: ${oB};
      border-color: ${oB};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:active
      .checked-indicator {
      background: ${tM};
      fill: ${tM};
    }

    :host([aria-checked="true"]:${K.focusVisible}:not([disabled])) .control {
      outline-offset: 2px;
      outline: solid calc(${ej} * 1px) ${tO};
    }

    :host([aria-invalid='true'][aria-checked="true"]:${K.focusVisible}:not([disabled])) .control {
      outline-color: ${oL};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
      cursor: ${K.disabledCursor};
    }

    :host([aria-checked='true']) .checked-indicator {
      opacity: 1;
    }

    :host([disabled]) {
      opacity: ${eD};
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      .control,
      :host([aria-checked='true']:not([disabled])) .control {
        forced-color-adjust: none;
        border-color: ${Z.FieldText};
        background: ${Z.Field};
      }
      :host([aria-invalid='true']) {
        border-style: dashed;
      }
      :host(:not([disabled])) .control:hover {
        border-color: ${Z.Highlight};
        background: ${Z.Field};
      }
      :host([aria-checked='true']:not([disabled])) .control:hover,
      :host([aria-checked='true']:not([disabled])) .control:active {
        border-color: ${Z.Highlight};
        background: ${Z.Highlight};
      }
      :host([aria-checked='true']) .checked-indicator {
        background: ${Z.Highlight};
        fill: ${Z.Highlight};
      }
      :host([aria-checked='true']:not([disabled]))
        .control:hover
        .checked-indicator,
      :host([aria-checked='true']:not([disabled]))
        .control:active
        .checked-indicator {
        background: ${Z.HighlightText};
        fill: ${Z.HighlightText};
      }
      :host(:${K.focusVisible}) .control {
        border-color: ${Z.Highlight};
        outline-offset: 2px;
        outline: solid calc(${ej} * 1px) ${Z.FieldText};
      }
      :host([aria-checked="true"]:${K.focusVisible}:not([disabled])) .control {
        border-color: ${Z.Highlight};
        outline: solid calc(${ej} * 1px) ${Z.FieldText};
      }
      :host([disabled]) {
        forced-color-adjust: none;
        opacity: 1;
      }
      :host([disabled]) .label {
        color: ${Z.GrayText};
      }
      :host([disabled]) .control,
      :host([aria-checked='true'][disabled]) .control:hover,
      .control:active {
        background: ${Z.Field};
        border-color: ${Z.GrayText};
      }
      :host([disabled]) .checked-indicator,
      :host([aria-checked='true'][disabled]) .control:hover .checked-indicator {
        fill: ${Z.GrayText};
        background: ${Z.GrayText};
      }
    `)),aA=(e,t)=>(0,o2.html)`
  <template
    role="radio"
    aria-checked="${e=>e.checked}"
    aria-required="${e=>e.required}"
    aria-disabled="${e=>e.disabled}"
    aria-readonly="${e=>e.readOnly}"
    @keypress="${(e,t)=>e.keypressHandler(t.event)}"
    @click="${(e,t)=>e.clickHandler(t.event)}"
  >
    <div part="control" class="control">
      <slot name="checked-indicator">
        ${t.checkedIndicator||""}
      </slot>
    </div>
    <label
      part="label"
      class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
    >
      <slot ${(0,o2.slotted)("defaultSlottedNodes")}></slot>
    </label>
  </template>
`;class aM extends K.Radio{}let aG=aM.compose({baseName:"radio",baseClass:K.Radio,template:aA,styles:aP,checkedIndicator:`
        <div part="checked-indicator" class="checked-indicator"></div>
    `}),aE=(e,t)=>(0,o2.css)`
  ${(0,K.display)("flex")} :host {
    align-items: flex-start;
    margin: calc(${eC} * 1px) 0;
    flex-direction: column;
  }
  .positioning-region {
    display: flex;
    flex-wrap: wrap;
  }
  :host([orientation='vertical']) .positioning-region {
    flex-direction: column;
  }
  :host([orientation='horizontal']) .positioning-region {
    flex-direction: row;
  }
`;class a_ extends K.RadioGroup{constructor(){super(),o2.Observable.getNotifier(this).subscribe({handleChange(e,t){"slottedRadioButtons"===t&&e.ariaInvalidChanged()}},"slottedRadioButtons")}ariaInvalidChanged(){this.slottedRadioButtons&&this.slottedRadioButtons.forEach(e=>{var t;e.setAttribute("aria-invalid",null!=(t=this.getAttribute("aria-invalid"))?t:"false")})}}let aq=a_.compose({baseName:"radio-group",baseClass:K.RadioGroup,template:K.radioGroupTemplate,styles:aE}),aW=K.DesignToken.create("clear-button-hover").withDefault(e=>{let t=t7.getValueFor(e),o=tQ.getValueFor(e);return t.evaluate(e,o.evaluate(e).hover).hover}),aU=K.DesignToken.create("clear-button-active").withDefault(e=>{let t=t7.getValueFor(e),o=tQ.getValueFor(e);return t.evaluate(e,o.evaluate(e).hover).active}),aX=(e,t)=>(0,o2.css)`
  ${r7}

  .control::-webkit-search-cancel-button {
    -webkit-appearance: none;
  }

  .control:hover,
    .control:${K.focusVisible},
    .control:disabled,
    .control:active {
    outline: none;
  }

  .clear-button {
    height: calc(100% - 2px);
    opacity: 0;
    margin: 1px;
    background: transparent;
    color: ${ov};
    fill: currentcolor;
    border: none;
    border-radius: calc(${ek} * 1px);
    min-width: calc(${o6} * 1px);
    font-size: ${ez};
    line-height: ${eB};
    outline: none;
    font-family: ${e$};
    padding: 0 calc((10 + (${eC} * 2 * ${eF})) * 1px);
  }

  .clear-button:hover {
    background: ${ot};
  }

  .clear-button:active {
    background: ${oo};
  }

  :host([appearance='filled']) .clear-button:hover {
    background: ${aW};
  }

  :host([appearance='filled']) .clear-button:active {
    background: ${aU};
  }

  .input-wrapper {
    display: flex;
    position: relative;
    width: 100%;
  }

  .start,
  .end {
    display: flex;
    margin: 1px;
    fill: currentcolor;
  }

  ::slotted([slot='end']) {
    height: 100%;
  }

  .end {
    margin-inline-end: 1px;
    height: calc(100% - 2px);
  }

  ::slotted(svg),
  ::slotted(jp-icon) {
    /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
    width: 16px;
    height: 16px;
    margin-inline-end: 11px;
    margin-inline-start: 11px;
    margin-top: auto;
    margin-bottom: auto;
  }

  .clear-button__hidden {
    opacity: 0;
  }

  :host(:hover:not([disabled], [readOnly])) .clear-button,
  :host(:active:not([disabled], [readOnly])) .clear-button,
  :host(:focus-within:not([disabled], [readOnly])) .clear-button {
    opacity: 1;
  }

  :host(:hover:not([disabled], [readOnly])) .clear-button__hidden,
  :host(:active:not([disabled], [readOnly])) .clear-button__hidden,
  :host(:focus-within:not([disabled], [readOnly])) .clear-button__hidden {
    opacity: 0;
  }
`;class aY extends K.Search{constructor(){super(...arguments),this.appearance="outline"}}re([o2.attr],aY.prototype,"appearance",void 0);let aZ=aY.compose({baseName:"search",baseClass:K.Search,template:K.searchTemplate,styles:aX,shadowOptions:{delegatesFocus:!0}});class aJ extends K.Select{constructor(){super(...arguments),this.listboxScrollWidth=""}autoWidthChanged(e,t){t?this.setAutoWidth():this.style.removeProperty("width")}setAutoWidth(){if(!this.autoWidth||!this.isConnected)return;let e=this.listbox.getBoundingClientRect().width;0===e&&this.listbox.hidden&&(Object.assign(this.listbox.style,{visibility:"hidden"}),this.listbox.removeAttribute("hidden"),e=this.listbox.getBoundingClientRect().width,this.listbox.setAttribute("hidden",""),this.listbox.style.removeProperty("visibility")),e>0&&Object.assign(this.style,{width:`${e}px`})}connectedCallback(){super.connectedCallback(),this.setAutoWidth(),this.listbox&&tz.setValueFor(this.listbox,tw)}slottedOptionsChanged(e,t){super.slottedOptionsChanged(e,t),this.setAutoWidth()}get listboxMaxHeight(){return Math.floor(this.maxHeight/oS.getValueFor(this)).toString()}listboxScrollWidthChanged(){this.updateComputedStylesheet()}get selectSize(){var e;return`${null!=(e=this.size)?e:4*!!this.multiple}`}multipleChanged(e,t){super.multipleChanged(e,t),this.updateComputedStylesheet()}maxHeightChanged(e,t){this.collapsible&&this.updateComputedStylesheet()}setPositioning(){super.setPositioning(),this.updateComputedStylesheet()}sizeChanged(e,t){(super.sizeChanged(e,t),this.updateComputedStylesheet(),this.collapsible)?requestAnimationFrame(()=>{this.listbox.style.setProperty("display","flex"),this.listbox.style.setProperty("overflow","visible"),this.listbox.style.setProperty("visibility","hidden"),this.listbox.style.setProperty("width","auto"),this.listbox.hidden=!1,this.listboxScrollWidth=`${this.listbox.scrollWidth}`,this.listbox.hidden=!0,this.listbox.style.removeProperty("display"),this.listbox.style.removeProperty("overflow"),this.listbox.style.removeProperty("visibility"),this.listbox.style.removeProperty("width")}):this.listboxScrollWidth=""}updateComputedStylesheet(){this.computedStylesheet&&this.$fastController.removeStyles(this.computedStylesheet),this.computedStylesheet=(0,o2.css)`
      :host {
        --listbox-max-height: ${this.listboxMaxHeight};
        --listbox-scroll-width: ${this.listboxScrollWidth};
        --size: ${this.selectSize};
      }
    `,this.$fastController.addStyles(this.computedStylesheet)}}re([(0,o2.attr)({attribute:"autowidth",mode:"boolean"})],aJ.prototype,"autoWidth",void 0),re([(0,o2.attr)({attribute:"minimal",mode:"boolean"})],aJ.prototype,"minimal",void 0),re([o2.attr],aJ.prototype,"scale",void 0),re([o2.observable],aJ.prototype,"listboxScrollWidth",void 0);let aK=aJ.compose({baseName:"select",baseClass:K.Select,template:K.selectTemplate,styles:r_,indicator:`
        <svg
            class="select-indicator"
            part="select-indicator"
            viewBox="0 0 12 7"
            xmlns="http://www.w3.org/2000/svg"
        >
            <path
                d="M11.85.65c.2.2.2.5 0 .7L6.4 6.84a.55.55 0 01-.78 0L.14 1.35a.5.5 0 11.71-.7L6 5.8 11.15.65c.2-.2.5-.2.7 0z"
            />
        </svg>
    `}),aQ=(e,t)=>(0,o2.css)`
    ${(0,K.display)("block")} :host {
      --skeleton-fill-default: #e1dfdd;
      overflow: hidden;
      width: 100%;
      position: relative;
      background-color: var(--skeleton-fill, var(--skeleton-fill-default));
      --skeleton-animation-gradient-default: linear-gradient(
        270deg,
        var(--skeleton-fill, var(--skeleton-fill-default)) 0%,
        #f3f2f1 51.13%,
        var(--skeleton-fill, var(--skeleton-fill-default)) 100%
      );
      --skeleton-animation-timing-default: ease-in-out;
    }

    :host([shape='rect']) {
      border-radius: calc(${ek} * 1px);
    }

    :host([shape='circle']) {
      border-radius: 100%;
      overflow: hidden;
    }

    object {
      position: absolute;
      width: 100%;
      height: auto;
      z-index: 2;
    }

    object img {
      width: 100%;
      height: auto;
    }

    ${(0,K.display)("block")} span.shimmer {
      position: absolute;
      width: 100%;
      height: 100%;
      background-image: var(
        --skeleton-animation-gradient,
        var(--skeleton-animation-gradient-default)
      );
      background-size: 0px 0px / 90% 100%;
      background-repeat: no-repeat;
      background-color: var(--skeleton-animation-fill, ${t0});
      animation: shimmer 2s infinite;
      animation-timing-function: var(
        --skeleton-animation-timing,
        var(--skeleton-timing-default)
      );
      animation-direction: normal;
      z-index: 1;
    }

    ::slotted(svg),
    ::slotted(jp-icon) {
      z-index: 2;
    }

    ::slotted(.pattern) {
      width: 100%;
      height: 100%;
    }

    @keyframes shimmer {
      0% {
        transform: translateX(-100%);
      }
      100% {
        transform: translateX(100%);
      }
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        forced-color-adjust: none;
        background-color: ${Z.ButtonFace};
        box-shadow: 0 0 0 1px ${Z.ButtonText};
      }

      ${(0,K.display)("block")} span.shimmer {
        display: none;
      }
    `));class a0 extends K.Skeleton{}let a1=a0.compose({baseName:"skeleton",baseClass:K.Skeleton,template:K.skeletonTemplate,styles:aQ}),a2=(0,o2.css)`
  .track-start {
    left: 0;
  }
`,a5=(0,o2.css)`
  .track-start {
    right: 0;
  }
`,a6=(e,t)=>(0,o2.css)`
    :host([hidden]) {
      display: none;
    }

    ${(0,K.display)("inline-grid")} :host {
      --thumb-size: calc(${o6} * 0.5 - ${eC});
      --thumb-translate: calc(
        var(--thumb-size) * -0.5 + var(--track-width) / 2
      );
      --track-overhang: calc((${eC} / 2) * -1);
      --track-width: ${eC};
      --jp-slider-height: calc(var(--thumb-size) * 10);
      align-items: center;
      width: 100%;
      margin: calc(${eC} * 1px) 0;
      user-select: none;
      box-sizing: border-box;
      border-radius: calc(${ek} * 1px);
      outline: none;
      cursor: pointer;
    }
    :host([orientation='horizontal']) .positioning-region {
      position: relative;
      margin: 0 8px;
      display: grid;
      grid-template-rows: calc(var(--thumb-size) * 1px) 1fr;
    }
    :host([orientation='vertical']) .positioning-region {
      position: relative;
      margin: 0 8px;
      display: grid;
      height: 100%;
      grid-template-columns: calc(var(--thumb-size) * 1px) 1fr;
    }

    :host(:${K.focusVisible}) .thumb-cursor {
      box-shadow:
        0 0 0 2px ${tz},
        0 0 0 calc((2 + ${ej}) * 1px) ${tO};
    }

    :host([aria-invalid='true']:${K.focusVisible}) .thumb-cursor {
      box-shadow:
        0 0 0 2px ${tz},
        0 0 0 calc((2 + ${ej}) * 1px) ${oL};
    }

    .thumb-container {
      position: absolute;
      height: calc(var(--thumb-size) * 1px);
      width: calc(var(--thumb-size) * 1px);
      transition: all 0.2s ease;
      color: ${ov};
      fill: currentcolor;
    }
    .thumb-cursor {
      border: none;
      width: calc(var(--thumb-size) * 1px);
      height: calc(var(--thumb-size) * 1px);
      background: ${ov};
      border-radius: calc(${ek} * 1px);
    }
    .thumb-cursor:hover {
      background: ${ov};
      border-color: ${oy};
    }
    .thumb-cursor:active {
      background: ${ov};
    }
    .track-start {
      background: ${tY};
      position: absolute;
      height: 100%;
      left: 0;
      border-radius: calc(${ek} * 1px);
    }
    :host([aria-invalid='true']) .track-start {
      background-color: ${oj};
    }
    :host([orientation='horizontal']) .thumb-container {
      transform: translateX(calc(var(--thumb-size) * 0.5px))
        translateY(calc(var(--thumb-translate) * 1px));
    }
    :host([orientation='vertical']) .thumb-container {
      transform: translateX(calc(var(--thumb-translate) * 1px))
        translateY(calc(var(--thumb-size) * 0.5px));
    }
    :host([orientation='horizontal']) {
      min-width: calc(var(--thumb-size) * 1px);
    }
    :host([orientation='horizontal']) .track {
      right: calc(var(--track-overhang) * 1px);
      left: calc(var(--track-overhang) * 1px);
      align-self: start;
      height: calc(var(--track-width) * 1px);
    }
    :host([orientation='vertical']) .track {
      top: calc(var(--track-overhang) * 1px);
      bottom: calc(var(--track-overhang) * 1px);
      width: calc(var(--track-width) * 1px);
      height: 100%;
    }
    .track {
      background: ${ox};
      position: absolute;
      border-radius: calc(${ek} * 1px);
    }
    :host([orientation='vertical']) {
      height: calc(var(--fast-slider-height) * 1px);
      min-height: calc(var(--thumb-size) * 1px);
      min-width: calc(${eC} * 20px);
    }
    :host([orientation='vertical']) .track-start {
      height: auto;
      width: 100%;
      top: 0;
    }
    :host([disabled]),
    :host([readonly]) {
      cursor: ${K.disabledCursor};
    }
    :host([disabled]) {
      opacity: ${eD};
    }
  `.withBehaviors(new rb(a2,a5),(0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      .thumb-cursor {
        forced-color-adjust: none;
        border-color: ${Z.FieldText};
        background: ${Z.FieldText};
      }
      .thumb-cursor:hover,
      .thumb-cursor:active {
        background: ${Z.Highlight};
      }
      .track {
        forced-color-adjust: none;
        background: ${Z.FieldText};
      }
      :host(:${K.focusVisible}) .thumb-cursor {
        border-color: ${Z.Highlight};
      }
      :host([disabled]) {
        opacity: 1;
      }
      :host([disabled]) .track,
      :host([disabled]) .thumb-cursor {
        forced-color-adjust: none;
        background: ${Z.GrayText};
      }

      :host(:${K.focusVisible}) .thumb-cursor {
        background: ${Z.Highlight};
        border-color: ${Z.Highlight};
        box-shadow:
          0 0 0 2px ${Z.Field},
          0 0 0 4px ${Z.FieldText};
      }
    `));class a3 extends K.Slider{}let a4=a3.compose({baseName:"slider",baseClass:K.Slider,template:K.sliderTemplate,styles:a6,thumb:`
        <div class="thumb-cursor"></div>
    `});var a9=o(66742);let a8=(0,o2.css)`
  :host {
    align-self: start;
    grid-row: 2;
    margin-top: -2px;
    height: calc((${o6} / 2 + ${eC}) * 1px);
    width: auto;
  }
  .container {
    grid-template-rows: auto auto;
    grid-template-columns: 0;
  }
  .label {
    margin: 2px 0;
  }
`,a7=(0,o2.css)`
  :host {
    justify-self: start;
    grid-column: 2;
    margin-left: 2px;
    height: auto;
    width: calc((${o6} / 2 + ${eC}) * 1px);
  }
  .container {
    grid-template-columns: auto auto;
    grid-template-rows: 0;
    min-width: calc(var(--thumb-size) * 1px);
    height: calc(var(--thumb-size) * 1px);
  }
  .mark {
    transform: rotate(90deg);
    align-self: center;
  }
  .label {
    margin-left: calc((${eC} / 2) * 3px);
    align-self: center;
  }
`,ie=(e,t)=>(0,o2.css)`
    ${(0,K.display)("block")} :host {
      font-family: ${e$};
      color: ${ov};
      fill: currentcolor;
    }
    .root {
      position: absolute;
      display: grid;
    }
    .container {
      display: grid;
      justify-self: center;
    }
    .label {
      justify-self: center;
      align-self: center;
      white-space: nowrap;
      max-width: 30px;
    }
    .mark {
      width: calc((${eC} / 4) * 1px);
      height: calc(${o6} * 0.25 * 1px);
      background: ${ox};
      justify-self: center;
    }
    :host(.disabled) {
      opacity: ${eD};
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      .mark {
        forced-color-adjust: none;
        background: ${Z.FieldText};
      }
      :host(.disabled) {
        forced-color-adjust: none;
        opacity: 1;
      }
      :host(.disabled) .label {
        color: ${Z.GrayText};
      }
      :host(.disabled) .mark {
        background: ${Z.GrayText};
      }
    `));class it extends K.SliderLabel{sliderOrientationChanged(){this.sliderOrientation===a9.t.horizontal?(this.$fastController.addStyles(a8),this.$fastController.removeStyles(a7)):(this.$fastController.addStyles(a7),this.$fastController.removeStyles(a8))}}let io=it.compose({baseName:"slider-label",baseClass:K.SliderLabel,template:K.sliderLabelTemplate,styles:ie}),ir=(e,t)=>(0,o2.css)`
    :host([hidden]) {
      display: none;
    }

    ${(0,K.display)("inline-flex")} :host {
      align-items: center;
      outline: none;
      font-family: ${e$};
      margin: calc(${eC} * 1px) 0;
      ${""} user-select: none;
    }

    :host([disabled]) {
      opacity: ${eD};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .switch,
    :host([disabled]) .switch {
      cursor: ${K.disabledCursor};
    }

    .switch {
      position: relative;
      outline: none;
      box-sizing: border-box;
      width: calc(${o6} * 1px);
      height: calc((${o6} / 2 + ${eC}) * 1px);
      background: ${t3};
      border-radius: calc(${ek} * 1px);
      border: calc(${eT} * 1px) solid ${ox};
    }

    :host([aria-invalid='true']) .switch {
      border-color: ${oj};
    }

    .switch:hover {
      background: ${t4};
      border-color: ${oy};
      cursor: pointer;
    }

    :host([disabled]) .switch:hover,
    :host([readonly]) .switch:hover {
      background: ${t4};
      border-color: ${oy};
      cursor: ${K.disabledCursor};
    }

    :host([aria-invalid='true'][disabled]) .switch:hover,
    :host([aria-invalid='true'][readonly]) .switch:hover {
      border-color: ${oz};
    }

    :host(:not([disabled])) .switch:active {
      background: ${t9};
      border-color: ${ow};
    }

    :host([aria-invalid='true']:not([disabled])) .switch:active {
      border-color: ${oB};
    }

    :host(:${K.focusVisible}) .switch {
      outline-offset: 2px;
      outline: solid calc(${ej} * 1px) ${tO};
    }

    :host([aria-invalid='true']:${K.focusVisible}) .switch {
      outline-color: ${oL};
    }

    .checked-indicator {
      position: absolute;
      top: 5px;
      bottom: 5px;
      background: ${ov};
      border-radius: calc(${ek} * 1px);
      transition: all 0.2s ease-in-out;
    }

    .status-message {
      color: ${ov};
      cursor: pointer;
      font-size: ${ez};
      line-height: ${eB};
    }

    :host([disabled]) .status-message,
    :host([readonly]) .status-message {
      cursor: ${K.disabledCursor};
    }

    .label {
      color: ${ov};
      margin-inline-end: calc(${eC} * 2px + 2px);
      font-size: ${ez};
      line-height: ${eB};
      cursor: pointer;
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    ::slotted([slot='checked-message']),
    ::slotted([slot='unchecked-message']) {
      margin-inline-start: calc(${eC} * 2px + 2px);
    }

    :host([aria-checked='true']) .checked-indicator {
      background: ${tP};
    }

    :host([aria-checked='true']) .switch {
      background: ${tL};
      border-color: ${tL};
    }

    :host([aria-checked='true']:not([disabled])) .switch:hover {
      background: ${tH};
      border-color: ${tH};
    }

    :host([aria-invalid='true'][aria-checked='true']) .switch {
      background-color: ${oj};
      border-color: ${oj};
    }

    :host([aria-invalid='true'][aria-checked='true']:not([disabled]))
      .switch:hover {
      background-color: ${oz};
      border-color: ${oz};
    }

    :host([aria-checked='true']:not([disabled]))
      .switch:hover
      .checked-indicator {
      background: ${tA};
    }

    :host([aria-checked='true']:not([disabled])) .switch:active {
      background: ${tN};
      border-color: ${tN};
    }

    :host([aria-invalid='true'][aria-checked='true']:not([disabled]))
      .switch:active {
      background-color: ${oB};
      border-color: ${oB};
    }

    :host([aria-checked='true']:not([disabled]))
      .switch:active
      .checked-indicator {
      background: ${tM};
    }

    :host([aria-checked="true"]:${K.focusVisible}:not([disabled])) .switch {
      outline: solid calc(${ej} * 1px) ${tO};
    }

    :host([aria-invalid='true'][aria-checked="true"]:${K.focusVisible}:not([disabled])) .switch {
      outline-color: ${oL};
    }

    .unchecked-message {
      display: block;
    }

    .checked-message {
      display: none;
    }

    :host([aria-checked='true']) .unchecked-message {
      display: none;
    }

    :host([aria-checked='true']) .checked-message {
      display: block;
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      .checked-indicator,
      :host(:not([disabled])) .switch:active .checked-indicator {
        forced-color-adjust: none;
        background: ${Z.FieldText};
      }
      .switch {
        forced-color-adjust: none;
        background: ${Z.Field};
        border-color: ${Z.FieldText};
      }
      :host([aria-invalid='true']) .switch {
        border-style: dashed;
      }
      :host(:not([disabled])) .switch:hover {
        background: ${Z.HighlightText};
        border-color: ${Z.Highlight};
      }
      :host([aria-checked='true']) .switch {
        background: ${Z.Highlight};
        border-color: ${Z.Highlight};
      }
      :host([aria-checked='true']:not([disabled])) .switch:hover,
      :host(:not([disabled])) .switch:active {
        background: ${Z.HighlightText};
        border-color: ${Z.Highlight};
      }
      :host([aria-checked='true']) .checked-indicator {
        background: ${Z.HighlightText};
      }
      :host([aria-checked='true']:not([disabled]))
        .switch:hover
        .checked-indicator {
        background: ${Z.Highlight};
      }
      :host([disabled]) {
        opacity: 1;
      }
      :host(:${K.focusVisible}) .switch {
        border-color: ${Z.Highlight};
        outline-offset: 2px;
        outline: solid calc(${ej} * 1px) ${Z.FieldText};
      }
      :host([aria-checked="true"]:${K.focusVisible}:not([disabled])) .switch {
        outline: solid calc(${ej} * 1px) ${Z.FieldText};
      }
      :host([disabled]) .checked-indicator {
        background: ${Z.GrayText};
      }
      :host([disabled]) .switch {
        background: ${Z.Field};
        border-color: ${Z.GrayText};
      }
    `),new rb((0,o2.css)`
        .checked-indicator {
          left: 5px;
          right: calc(((${o6} / 2) + 1) * 1px);
        }

        :host([aria-checked='true']) .checked-indicator {
          left: calc(((${o6} / 2) + 1) * 1px);
          right: 5px;
        }
      `,(0,o2.css)`
        .checked-indicator {
          right: 5px;
          left: calc(((${o6} / 2) + 1) * 1px);
        }

        :host([aria-checked='true']) .checked-indicator {
          right: calc(((${o6} / 2) + 1) * 1px);
          left: 5px;
        }
      `));class ia extends K.Switch{}let ii=ia.compose({baseName:"switch",baseClass:K.Switch,template:K.switchTemplate,styles:ir,switch:`
        <span class="checked-indicator" part="checked-indicator"></span>
    `}),il=(e,t)=>(0,o2.css)`
  ${(0,K.display)("block")} :host {
    box-sizing: border-box;
    font-size: ${ez};
    line-height: ${eB};
    padding: 0 calc((6 + (${eC} * 2 * ${eF})) * 1px);
  }
`;class is extends K.TabPanel{}let ic=is.compose({baseName:"tab-panel",baseClass:K.TabPanel,template:K.tabPanelTemplate,styles:il}),id=(e,t)=>(0,o2.css)`
    ${(0,K.display)("inline-flex")} :host {
      box-sizing: border-box;
      font-family: ${e$};
      font-size: ${ez};
      line-height: ${eB};
      height: calc(${o6} * 1px);
      padding: calc(${eC} * 5px) calc(${eC} * 4px);
      color: ${of};
      fill: currentcolor;
      border-radius: 0 0 calc(${ek} * 1px)
        calc(${ek} * 1px);
      border: calc(${eT} * 1px) solid transparent;
      align-items: center;
      justify-content: center;
      grid-row: 2;
      cursor: pointer;
    }

    :host(:hover) {
      color: ${ov};
      fill: currentcolor;
    }

    :host(:active) {
      color: ${ov};
      fill: currentcolor;
    }

    :host([disabled]) {
      cursor: ${K.disabledCursor};
      opacity: ${eD};
    }

    :host([disabled]:hover) {
      color: ${of};
      background: ${oe};
    }

    :host([aria-selected='true']) {
      background: ${t0};
      color: ${ov};
      fill: currentcolor;
    }

    :host([aria-selected='true']:hover) {
      background: ${t1};
      color: ${ov};
      fill: currentcolor;
    }

    :host([aria-selected='true']:active) {
      background: ${t2};
      color: ${ov};
      fill: currentcolor;
    }

    :host(:${K.focusVisible}) {
      outline: none;
      border-color: ${tO};
      box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
        ${tO};
    }

    :host(:focus) {
      outline: none;
    }

    :host(.vertical) {
      justify-content: end;
      grid-column: 2;
      border-bottom-left-radius: 0;
      border-top-right-radius: calc(${ek} * 1px);
    }

    :host(.vertical[aria-selected='true']) {
      z-index: 2;
    }

    :host(.vertical:hover) {
      color: ${ov};
    }

    :host(.vertical:active) {
      color: ${ov};
    }

    :host(.vertical:hover[aria-selected='true']) {
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        forced-color-adjust: none;
        border-color: transparent;
        color: ${Z.ButtonText};
        fill: currentcolor;
      }
      :host(:hover),
      :host(.vertical:hover),
      :host([aria-selected='true']:hover) {
        background: ${Z.Highlight};
        color: ${Z.HighlightText};
        fill: currentcolor;
      }
      :host([aria-selected='true']) {
        background: ${Z.HighlightText};
        color: ${Z.Highlight};
        fill: currentcolor;
      }
      :host(:${K.focusVisible}) {
        border-color: ${Z.ButtonText};
        box-shadow: none;
      }
      :host([disabled]),
      :host([disabled]:hover) {
        opacity: 1;
        color: ${Z.GrayText};
        background: ${Z.ButtonFace};
      }
    `));class ih extends K.Tab{}let iu=ih.compose({baseName:"tab",baseClass:K.Tab,template:K.tabTemplate,styles:id}),ip=(e,t)=>(0,o2.css)`
    ${(0,K.display)("grid")} :host {
      box-sizing: border-box;
      font-family: ${e$};
      font-size: ${ez};
      line-height: ${eB};
      color: ${ov};
      grid-template-columns: auto 1fr auto;
      grid-template-rows: auto 1fr;
    }

    .tablist {
      display: grid;
      grid-template-rows: auto auto;
      grid-template-columns: auto;
      position: relative;
      width: max-content;
      align-self: end;
      padding: calc(${eC} * 4px) calc(${eC} * 4px) 0;
      box-sizing: border-box;
    }

    .start,
    .end {
      align-self: center;
    }

    .activeIndicator {
      grid-row: 1;
      grid-column: 1;
      width: 100%;
      height: 4px;
      justify-self: center;
      background: ${tL};
      margin-top: 0;
      border-radius: calc(${ek} * 1px)
        calc(${ek} * 1px) 0 0;
    }

    .activeIndicatorTransition {
      transition: transform 0.01s ease-in-out;
    }

    .tabpanel {
      grid-row: 2;
      grid-column-start: 1;
      grid-column-end: 4;
      position: relative;
    }

    :host([orientation='vertical']) {
      grid-template-rows: auto 1fr auto;
      grid-template-columns: auto 1fr;
    }

    :host([orientation='vertical']) .tablist {
      grid-row-start: 2;
      grid-row-end: 2;
      display: grid;
      grid-template-rows: auto;
      grid-template-columns: auto 1fr;
      position: relative;
      width: max-content;
      justify-self: end;
      align-self: flex-start;
      width: 100%;
      padding: 0 calc(${eC} * 4px)
        calc((${o6} - ${eC}) * 1px) 0;
    }

    :host([orientation='vertical']) .tabpanel {
      grid-column: 2;
      grid-row-start: 1;
      grid-row-end: 4;
    }

    :host([orientation='vertical']) .end {
      grid-row: 3;
    }

    :host([orientation='vertical']) .activeIndicator {
      grid-column: 1;
      grid-row: 1;
      width: 4px;
      height: 100%;
      margin-inline-end: 0px;
      align-self: center;
      background: ${tL};
      border-radius: calc(${ek} * 1px) 0 0
        calc(${ek} * 1px);
    }

    :host([orientation='vertical']) .activeIndicatorTransition {
      transition: transform 0.01s ease-in-out;
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      .activeIndicator,
      :host([orientation='vertical']) .activeIndicator {
        forced-color-adjust: none;
        background: ${Z.Highlight};
      }
    `));class ig extends K.Tabs{}let ib=ig.compose({baseName:"tabs",baseClass:K.Tabs,template:K.tabsTemplate,styles:ip}),im=(e,t)=>(0,o2.css)`
    ${(0,K.display)("inline-block")} :host {
      font-family: ${e$};
      outline: none;
      user-select: none;
    }

    .control {
      box-sizing: border-box;
      position: relative;
      color: ${ov};
      background: ${t3};
      border-radius: calc(${ek} * 1px);
      border: calc(${eT} * 1px) solid ${oi};
      height: calc(${o6} * 2px);
      font: inherit;
      font-size: ${ez};
      line-height: ${eB};
      padding: calc(${eC} * 2px + 1px);
      width: 100%;
      resize: none;
    }

    :host([aria-invalid='true']) .control {
      border-color: ${oj};
    }

    .control:hover:enabled {
      background: ${t4};
      border-color: ${ol};
    }

    :host([aria-invalid='true']) .control:hover:enabled {
      border-color: ${oz};
    }

    .control:active:enabled {
      background: ${t9};
      border-color: ${os};
    }

    :host([aria-invalid='true']) .control:active:enabled {
      border-color: ${oB};
    }

    .control:hover,
    .control:${K.focusVisible},
    .control:disabled,
    .control:active {
      outline: none;
    }

    :host(:focus-within) .control {
      border-color: ${tO};
      box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
        ${tO};
    }

    :host([aria-invalid='true']:focus-within) .control {
      border-color: ${oL};
      box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
        ${oL};
    }

    :host([appearance='filled']) .control {
      background: ${t0};
    }

    :host([appearance='filled']:hover:not([disabled])) .control {
      background: ${t1};
    }

    :host([resize='both']) .control {
      resize: both;
    }

    :host([resize='horizontal']) .control {
      resize: horizontal;
    }

    :host([resize='vertical']) .control {
      resize: vertical;
    }

    .label {
      display: block;
      color: ${ov};
      cursor: pointer;
      font-size: ${ez};
      line-height: ${eB};
      margin-bottom: 4px;
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
      cursor: ${K.disabledCursor};
    }
    :host([disabled]) {
      opacity: ${eD};
    }
    :host([disabled]) .control {
      border-color: ${ox};
    }

    :host([cols]) {
      width: initial;
    }

    :host([rows]) .control {
      height: initial;
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host([disabled]) {
        opacity: 1;
      }

      :host([aria-invalid='true']) .control {
        border-style: dashed;
      }
    `));class iv extends K.TextArea{constructor(){super(...arguments),this.appearance="outline"}}re([o2.attr],iv.prototype,"appearance",void 0);let i$=iv.compose({baseName:"text-area",baseClass:K.TextArea,template:K.textAreaTemplate,styles:im,shadowOptions:{delegatesFocus:!0}}),ix=(e,t)=>(0,o2.css)`
  ${r7}

  .start,
    .end {
    display: flex;
  }
`;class iy extends K.TextField{constructor(){super(...arguments),this.appearance="outline"}}re([o2.attr],iy.prototype,"appearance",void 0);let iw=iy.compose({baseName:"text-field",baseClass:K.TextField,template:K.textFieldTemplate,styles:ix,shadowOptions:{delegatesFocus:!0}});var ik=o(92017),iF=o(13066);let iC=(e,t)=>(0,o2.css)`
    ${(0,K.display)("inline-flex")} :host {
      --toolbar-item-gap: calc(
        (var(--design-unit) + calc(var(--density) + 2)) * 1px
      );
      background-color: ${tz};
      border-radius: calc(${ek} * 1px);
      fill: currentcolor;
      padding: var(--toolbar-item-gap);
    }

    :host(${K.focusVisible}) {
      outline: calc(${eT} * 1px) solid ${tO};
    }

    .positioning-region {
      align-items: flex-start;
      display: inline-flex;
      flex-flow: row wrap;
      justify-content: flex-start;
      width: 100%;
      height: 100%;
    }

    :host([orientation='vertical']) .positioning-region {
      flex-direction: column;
    }

    ::slotted(:not([slot])) {
      flex: 0 0 auto;
      margin: 0 var(--toolbar-item-gap);
    }

    :host([orientation='vertical']) ::slotted(:not([slot])) {
      margin: var(--toolbar-item-gap) 0;
    }

    .start,
    .end {
      display: flex;
      margin: auto;
      margin-inline: 0;
    }

    ::slotted(svg),
    ::slotted(jp-icon) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host(:${K.focusVisible}) {
        box-shadow: 0 0 0 calc(${ej} * 1px)
          ${Z.Highlight};
        color: ${Z.ButtonText};
        forced-color-adjust: none;
      }
    `)),iS=Object.freeze({[r5.Is.ArrowUp]:{[a9.t.vertical]:-1},[r5.Is.ArrowDown]:{[a9.t.vertical]:1},[r5.Is.ArrowLeft]:{[a9.t.horizontal]:{[Q.O.ltr]:-1,[Q.O.rtl]:1}},[r5.Is.ArrowRight]:{[a9.t.horizontal]:{[Q.O.ltr]:1,[Q.O.rtl]:-1}}});class iV extends K.FoundationElement{constructor(){super(...arguments),this._activeIndex=0,this.direction=Q.O.ltr,this.orientation=a9.t.horizontal}get activeIndex(){return o2.Observable.track(this,"activeIndex"),this._activeIndex}set activeIndex(e){this.$fastController.isConnected&&(this._activeIndex=(0,ik.AB)(0,this.focusableElements.length-1,e),o2.Observable.notify(this,"activeIndex"))}slottedItemsChanged(){this.$fastController.isConnected&&this.reduceFocusableElements()}mouseDownHandler(e){var t;let o=null==(t=this.focusableElements)?void 0:t.findIndex(t=>t.contains(e.target));return o>-1&&this.activeIndex!==o&&this.setFocusedElement(o),!0}childItemsChanged(e,t){this.$fastController.isConnected&&this.reduceFocusableElements()}connectedCallback(){super.connectedCallback(),this.direction=(0,K.getDirection)(this)}focusinHandler(e){let t=e.relatedTarget;!t||this.contains(t)||this.setFocusedElement()}getDirectionalIncrementer(e){var t,o,r,a,i;return null!=(i=null!=(r=null==(o=null==(t=iS[e])?void 0:t[this.orientation])?void 0:o[this.direction])?r:null==(a=iS[e])?void 0:a[this.orientation])?i:0}keydownHandler(e){let t=e.key;if(!(t in r5.Is)||e.defaultPrevented||e.shiftKey)return!0;let o=this.getDirectionalIncrementer(t);if(!o)return!e.target.closest("[role=radiogroup]");let r=this.activeIndex+o;return this.focusableElements[r]&&e.preventDefault(),this.setFocusedElement(r),!0}get allSlottedItems(){return[...this.start.assignedElements(),...this.slottedItems,...this.end.assignedElements()]}reduceFocusableElements(){var e;let t=null==(e=this.focusableElements)?void 0:e[this.activeIndex];this.focusableElements=this.allSlottedItems.reduce(iV.reduceFocusableItems,[]);let o=this.focusableElements.indexOf(t);this.activeIndex=Math.max(0,o),this.setFocusableElements()}setFocusedElement(e=this.activeIndex){this.activeIndex=e,this.setFocusableElements(),this.focusableElements[this.activeIndex]&&this.contains(document.activeElement)&&this.focusableElements[this.activeIndex].focus()}static reduceFocusableItems(e,t){var o,r,a,i;let l="radio"===t.getAttribute("role"),s=null==(r=null==(o=t.$fastController)?void 0:o.definition.shadowOptions)?void 0:r.delegatesFocus,n=Array.from(null!=(i=null==(a=t.shadowRoot)?void 0:a.querySelectorAll("*"))?i:[]).some(e=>(0,iF.tp)(e));return!t.hasAttribute("disabled")&&!t.hasAttribute("hidden")&&((0,iF.tp)(t)||l||s||n)?(e.push(t),e):t.childElementCount?e.concat(Array.from(t.children).reduce(iV.reduceFocusableItems,[])):e}setFocusableElements(){this.$fastController.isConnected&&this.focusableElements.length>0&&this.focusableElements.forEach((e,t)=>{e.tabIndex=this.activeIndex===t?0:-1})}}re([o2.observable],iV.prototype,"direction",void 0),re([o2.attr],iV.prototype,"orientation",void 0),re([o2.observable],iV.prototype,"slottedItems",void 0),re([o2.observable],iV.prototype,"slottedLabel",void 0),re([o2.observable],iV.prototype,"childItems",void 0);class iD{}re([(0,o2.attr)({attribute:"aria-labelledby"})],iD.prototype,"ariaLabelledby",void 0),re([(0,o2.attr)({attribute:"aria-label"})],iD.prototype,"ariaLabel",void 0),(0,K.applyMixins)(iD,K.ARIAGlobalStatesAndProperties),(0,K.applyMixins)(iV,K.StartEnd,iD);class iT extends iV{}let ij=iT.compose({baseName:"toolbar",baseClass:iV,template:K.toolbarTemplate,styles:iC,shadowOptions:{delegatesFocus:!0}}),iz=(e,t)=>{let o=e.tagFor(K.AnchoredRegion);return(0,o2.css)`
    :host {
      contain: size;
      overflow: visible;
      height: 0;
      width: 0;
    }

    .tooltip {
      box-sizing: border-box;
      border-radius: calc(${ek} * 1px);
      border: calc(${eT} * 1px) solid ${ou};
      box-shadow: 0 0 0 1px ${ou} inset;
      background: ${t0};
      color: ${ov};
      padding: 4px;
      height: fit-content;
      width: fit-content;
      font-family: ${e$};
      font-size: ${ez};
      line-height: ${eB};
      white-space: nowrap;
      /* TODO: a mechanism to manage z-index across components
                    https://github.com/microsoft/fast/issues/3813 */
      z-index: 10000;
    }

    ${o} {
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: visible;
      flex-direction: row;
    }

    ${o}.right,
    ${o}.left {
      flex-direction: column;
    }

    ${o}.top .tooltip {
      margin-bottom: 4px;
    }

    ${o}.bottom .tooltip {
      margin-top: 4px;
    }

    ${o}.left .tooltip {
      margin-right: 4px;
    }

    ${o}.right .tooltip {
      margin-left: 4px;
    }

    ${o}.top.left .tooltip,
            ${o}.top.right .tooltip {
      margin-bottom: 0px;
    }

    ${o}.bottom.left .tooltip,
            ${o}.bottom.right .tooltip {
      margin-top: 0px;
    }

    ${o}.top.left .tooltip,
            ${o}.bottom.left .tooltip {
      margin-right: 0px;
    }

    ${o}.top.right .tooltip,
            ${o}.bottom.right .tooltip {
      margin-left: 0px;
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host([disabled]) {
        opacity: 1;
      }
    `))};class iB extends K.Tooltip{}let iL=iB.compose({baseName:"tooltip",baseClass:K.Tooltip,template:K.tooltipTemplate,styles:iz}),iH=(0,o2.cssPartial)`(((${ex} + ${eF}) * 0.5 + 2) * ${eC})`,iN=(0,o2.css)`
  .expand-collapse-glyph {
    transform: rotate(0deg);
  }
  :host(.nested) .expand-collapse-button {
    left: var(
      --expand-collapse-button-nested-width,
      calc(
        (
            ${iH} +
              ((${ex} + ${eF}) * 1.25)
          ) * -1px
      )
    );
  }
  :host([selected])::after {
    left: calc(${ej} * 1px);
  }
  :host([expanded]) > .positioning-region .expand-collapse-glyph {
    transform: rotate(90deg);
  }
`,iO=(0,o2.css)`
  .expand-collapse-glyph {
    transform: rotate(180deg);
  }
  :host(.nested) .expand-collapse-button {
    right: var(
      --expand-collapse-button-nested-width,
      calc(
        (
            ${iH} +
              ((${ex} + ${eF}) * 1.25)
          ) * -1px
      )
    );
  }
  :host([selected])::after {
    right: calc(${ej} * 1px);
  }
  :host([expanded]) > .positioning-region .expand-collapse-glyph {
    transform: rotate(90deg);
  }
`,iI=K.DesignToken.create("tree-item-expand-collapse-hover").withDefault(e=>{let t=t7.getValueFor(e);return t.evaluate(e,t.evaluate(e).hover).hover}),iR=K.DesignToken.create("tree-item-expand-collapse-selected-hover").withDefault(e=>{let t=tQ.getValueFor(e);return t7.getValueFor(e).evaluate(e,t.evaluate(e).rest).hover}),iP=(e,t)=>(0,o2.css)`
    /**
     * This animation exists because when tree item children are conditionally loaded
     * there is a visual bug where the DOM exists but styles have not yet been applied (essentially FOUC).
     * This subtle animation provides a ever so slight timing adjustment for loading that solves the issue.
     */
    @keyframes treeItemLoading {
      0% {
        opacity: 0;
      }
      100% {
        opacity: 1;
      }
    }

    ${(0,K.display)("block")} :host {
      contain: content;
      position: relative;
      outline: none;
      color: ${ov};
      background: ${oe};
      cursor: pointer;
      font-family: ${e$};
      --tree-item-nested-width: 0;
    }

    :host(:focus) > .positioning-region {
      outline: none;
    }

    :host(:focus) .content-region {
      outline: none;
    }

    :host(:${K.focusVisible}) .positioning-region {
      border-color: ${tO};
      box-shadow: 0 0 0 calc((${ej} - ${eT}) * 1px)
        ${tO} inset;
      color: ${ov};
    }

    .positioning-region {
      display: flex;
      position: relative;
      box-sizing: border-box;
      background: ${oe};
      border: transparent calc(${eT} * 1px) solid;
      border-radius: calc(${ek} * 1px);
      height: calc((${o6} + 1) * 1px);
    }

    .positioning-region::before {
      content: '';
      display: block;
      width: var(--tree-item-nested-width);
      flex-shrink: 0;
    }

    :host(:not([disabled])) .positioning-region:hover {
      background: ${ot};
    }

    :host(:not([disabled])) .positioning-region:active {
      background: ${oo};
    }

    .content-region {
      display: inline-flex;
      align-items: center;
      white-space: nowrap;
      width: 100%;
      min-width: 0;
      height: calc(${o6} * 1px);
      margin-inline-start: calc(${eC} * 2px + 8px);
      font-size: ${ez};
      line-height: ${eB};
      font-weight: 400;
    }

    .items {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      font-size: calc(1em + (${eC} + 16) * 1px);
    }

    .expand-collapse-button {
      background: none;
      border: none;
      outline: none;
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: calc(${iH} * 1px);
      height: calc(${iH} * 1px);
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      margin-left: 6px;
      margin-right: 6px;
    }

    .expand-collapse-glyph {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: calc((16 + ${eF}) * 1px);
      height: calc((16 + ${eF}) * 1px);
      transition: transform 0.1s linear;

      pointer-events: none;
      fill: currentcolor;
    }

    .start,
    .end {
      display: flex;
      fill: currentcolor;
    }

    ::slotted(svg),
    ::slotted(jp-icon) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;

      /* Something like that would do if the typography is adaptive
      font-size: inherit;
      width: ${eI};
      height: ${eI};
      */
    }

    .start {
      /* TODO: horizontalSpacing https://github.com/microsoft/fast/issues/2766 */
      margin-inline-end: calc(${eC} * 2px + 2px);
    }

    .end {
      /* TODO: horizontalSpacing https://github.com/microsoft/fast/issues/2766 */
      margin-inline-start: calc(${eC} * 2px + 2px);
    }

    :host([expanded]) > .items {
      animation: treeItemLoading ease-in 10ms;
      animation-iteration-count: 1;
      animation-fill-mode: forwards;
    }

    :host([disabled]) .content-region {
      opacity: ${eD};
      cursor: ${K.disabledCursor};
    }

    :host(.nested) .content-region {
      position: relative;
      /* Add left margin to collapse button size */
      margin-inline-start: calc(
        (
            ${iH} +
              ((${ex} + ${eF}) * 1.25)
          ) * 1px
      );
    }

    :host(.nested) .expand-collapse-button {
      position: absolute;
    }

    :host(.nested:not([disabled])) .expand-collapse-button:hover {
      background: ${iI};
    }

    :host([selected]) .positioning-region {
      background: ${t0};
    }

    :host([selected]:not([disabled])) .positioning-region:hover {
      background: ${t1};
    }

    :host([selected]:not([disabled])) .positioning-region:active {
      background: ${t2};
    }

    :host([selected]:not([disabled])) .expand-collapse-button:hover {
      background: ${iR};
    }

    :host([selected])::after {
      /* The background needs to be calculated based on the selected background state
         for this control. We currently have no way of changing that, so setting to
         accent-foreground-rest for the time being */
      background: ${tY};
      border-radius: calc(${ek} * 1px);
      content: '';
      display: block;
      position: absolute;
      top: calc((${o6} / 4) * 1px);
      width: 3px;
      height: calc((${o6} / 2) * 1px);
    }

    ::slotted(${e.tagFor(K.TreeItem)}) {
      --tree-item-nested-width: 1em;
      --expand-collapse-button-nested-width: calc(
        (
            ${iH} +
              ((${ex} + ${eF}) * 1.25)
          ) * -1px
      );
    }
  `.withBehaviors(new rb(iN,iO),(0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        forced-color-adjust: none;
        border-color: transparent;
        background: ${Z.Field};
        color: ${Z.FieldText};
      }
      :host .content-region .expand-collapse-glyph {
        fill: ${Z.FieldText};
      }
      :host .positioning-region:hover,
      :host([selected]) .positioning-region {
        background: ${Z.Highlight};
      }
      :host .positioning-region:hover .content-region,
      :host([selected]) .positioning-region .content-region {
        color: ${Z.HighlightText};
      }
      :host .positioning-region:hover .content-region .expand-collapse-glyph,
      :host .positioning-region:hover .content-region .start,
      :host .positioning-region:hover .content-region .end,
      :host([selected]) .content-region .expand-collapse-glyph,
      :host([selected]) .content-region .start,
      :host([selected]) .content-region .end {
        fill: ${Z.HighlightText};
      }
      :host([selected])::after {
        background: ${Z.Field};
      }
      :host(:${K.focusVisible}) .positioning-region {
        border-color: ${Z.FieldText};
        box-shadow: 0 0 0 2px inset ${Z.Field};
        color: ${Z.FieldText};
      }
      :host([disabled]) .content-region,
      :host([disabled]) .positioning-region:hover .content-region {
        opacity: 1;
        color: ${Z.GrayText};
      }
      :host([disabled]) .content-region .expand-collapse-glyph,
      :host([disabled]) .content-region .start,
      :host([disabled]) .content-region .end,
      :host([disabled])
        .positioning-region:hover
        .content-region
        .expand-collapse-glyph,
      :host([disabled]) .positioning-region:hover .content-region .start,
      :host([disabled]) .positioning-region:hover .content-region .end {
        fill: ${Z.GrayText};
      }
      :host([disabled]) .positioning-region:hover {
        background: ${Z.Field};
      }
      .expand-collapse-glyph,
      .start,
      .end {
        fill: ${Z.FieldText};
      }
      :host(.nested) .expand-collapse-button:hover {
        background: ${Z.Field};
      }
      :host(.nested) .expand-collapse-button:hover .expand-collapse-glyph {
        fill: ${Z.FieldText};
      }
    `));class iA extends K.TreeItem{}let iM=iA.compose({baseName:"tree-item",baseClass:K.TreeItem,template:K.treeItemTemplate,styles:iP,expandCollapseGlyph:`
        <svg
            viewBox="0 0 16 16"
            xmlns="http://www.w3.org/2000/svg"
            class="expand-collapse-glyph"
        >
            <path
                d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"
            />
        </svg>
    `}),iG=(e,t)=>(0,o2.css)`
  ${(0,K.display)("flex")} :host {
    flex-direction: column;
    align-items: stretch;
    min-width: fit-content;
    font-size: 0;
  }

  :host:focus-visible {
    outline: none;
  }
`;class iE extends K.TreeView{handleClick(e){if(e.defaultPrevented)return;if(!(e.target instanceof Element))return!0;let t=e.target;for(;t&&!(0,K.isTreeItemElement)(t);)(t=t.parentElement)===this&&(t=null);t&&!t.disabled&&(t.selected=!0)}}let i_=iE.compose({baseName:"tree-view",baseClass:K.TreeView,template:K.treeViewTemplate,styles:iG}),iq=(e,t)=>(0,o2.css)`
  .region {
    z-index: 1000;
    overflow: hidden;
    display: flex;
    font-family: ${e$};
    font-size: ${ez};
  }

  .loaded {
    opacity: 1;
    pointer-events: none;
  }

  .loading-display,
  .no-options-display {
    background: ${tz};
    width: 100%;
    min-height: calc(${o6} * 1px);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-items: center;
    padding: calc(${eC} * 1px);
  }

  .loading-progress {
    width: 42px;
    height: 42px;
  }

  .bottom {
    flex-direction: column;
  }

  .top {
    flex-direction: column-reverse;
  }
`,iW=(e,t)=>(0,o2.css)`
    :host {
      background: ${tz};
      --elevation: 11;
      /* TODO: a mechanism to manage z-index across components
            https://github.com/microsoft/fast/issues/3813 */
      z-index: 1000;
      display: flex;
      width: 100%;
      max-height: 100%;
      min-height: 58px;
      box-sizing: border-box;
      flex-direction: column;
      overflow-y: auto;
      overflow-x: hidden;
      pointer-events: auto;
      border-radius: calc(${ek} * 1px);
      padding: calc(${eC} * 1px) 0;
      border: calc(${eT} * 1px) solid transparent;
      ${rN}
    }

    .suggestions-available-alert {
      height: 0;
      opacity: 0;
      overflow: hidden;
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        background: ${Z.Canvas};
        border-color: ${Z.CanvasText};
      }
    `)),iU=(e,t)=>(0,o2.css)`
    :host {
      display: flex;
      align-items: center;
      justify-items: center;
      font-family: ${e$};
      border-radius: calc(${ek} * 1px);
      border: calc(${ej} * 1px) solid transparent;
      box-sizing: border-box;
      background: ${oe};
      color: ${ov};
      cursor: pointer;
      fill: currentcolor;
      font-size: ${ez};
      min-height: calc(${o6} * 1px);
      line-height: ${eB};
      margin: 0 calc(${eC} * 1px);
      outline: none;
      overflow: hidden;
      padding: 0 calc(${eC} * 2.25px);
      user-select: none;
      white-space: nowrap;
    }

    :host(:${K.focusVisible}[role="listitem"]) {
      border-color: ${ou};
      background: ${or};
    }

    :host(:hover) {
      background: ${ot};
    }

    :host(:active) {
      background: ${oo};
    }

    :host([aria-selected='true']) {
      background: ${tL};
      color: ${tP};
    }

    :host([aria-selected='true']:hover) {
      background: ${tH};
      color: ${tA};
    }

    :host([aria-selected='true']:active) {
      background: ${tN};
      color: ${tM};
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        border-color: transparent;
        forced-color-adjust: none;
        color: ${Z.ButtonText};
        fill: currentcolor;
      }

      :host(:not([aria-selected='true']):hover),
      :host([aria-selected='true']) {
        background: ${Z.Highlight};
        color: ${Z.HighlightText};
      }

      :host([disabled]),
      :host([disabled]:not([aria-selected='true']):hover) {
        background: ${Z.Canvas};
        color: ${Z.GrayText};
        fill: currentcolor;
        opacity: 1;
      }
    `)),iX=(e,t)=>(0,o2.css)`
    :host {
      display: flex;
      align-items: center;
      justify-items: center;
      font-family: ${e$};
      border-radius: calc(${ek} * 1px);
      border: calc(${ej} * 1px) solid transparent;
      box-sizing: border-box;
      background: ${oe};
      color: ${ov};
      cursor: pointer;
      fill: currentcolor;
      font-size: ${ez};
      height: calc(${o6} * 1px);
      line-height: ${eB};
      outline: none;
      overflow: hidden;
      padding: 0 calc(${eC} * 2.25px);
      user-select: none;
      white-space: nowrap;
    }

    :host(:hover) {
      background: ${ot};
    }

    :host(:active) {
      background: ${oo};
    }

    :host(:${K.focusVisible}) {
      background: ${or};
      border-color: ${ou};
    }

    :host([aria-selected='true']) {
      background: ${tL};
      color: ${tM};
    }
  `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      :host {
        border-color: transparent;
        forced-color-adjust: none;
        color: ${Z.ButtonText};
        fill: currentcolor;
      }

      :host(:not([aria-selected='true']):hover),
      :host([aria-selected='true']) {
        background: ${Z.Highlight};
        color: ${Z.HighlightText};
      }

      :host([disabled]),
      :host([disabled]:not([aria-selected='true']):hover) {
        background: ${Z.Canvas};
        color: ${Z.GrayText};
        fill: currentcolor;
        opacity: 1;
      }
    `));class iY extends K.Picker{}let iZ=iY.compose({baseName:"draft-picker",baseClass:K.Picker,template:K.pickerTemplate,styles:iq,shadowOptions:{}});class iJ extends K.PickerMenu{connectedCallback(){tz.setValueFor(this,tw),super.connectedCallback()}}let iK=iJ.compose({baseName:"draft-picker-menu",baseClass:K.PickerMenu,template:K.pickerMenuTemplate,styles:iW});class iQ extends K.PickerMenuOption{}let i0=iQ.compose({baseName:"draft-picker-menu-option",baseClass:K.PickerMenuOption,template:K.pickerMenuOptionTemplate,styles:iU});class i1 extends K.PickerList{}let i2=i1.compose({baseName:"draft-picker-list",baseClass:K.PickerList,template:K.pickerListTemplate,styles:(e,t)=>(0,o2.css)`
        :host {
            display: flex;
            flex-direction: row;
            column-gap: calc(${eC} * 1px);
            row-gap: calc(${eC} * 1px);
            flex-wrap: wrap;
        }

        ::slotted([role="combobox"]) {
            min-width: 260px;
            width: auto;
            box-sizing: border-box;
            color: ${ov};
            background: ${t3};
            border-radius: calc(${ek} * 1px);
            border: calc(${eT} * 1px) solid ${tL};
            height: calc(${o6} * 1px);
            font-family: ${e$};
            outline: none;
            user-select: none;
            font-size: ${ez};
            line-height: ${eB};
            padding: 0 calc(${eC} * 2px + 1px);
        }

        ::slotted([role="combobox"]:active) { {
            background: ${t4};
            border-color: ${tN};
        }

        ::slotted([role="combobox"]:focus-within) {
            border-color: ${ou};
            box-shadow: 0 0 0 1px ${ou} inset;
        }
    `.withBehaviors((0,K.forcedColorsStylesheetBehavior)((0,o2.css)`
      ::slotted([role='combobox']:active) {
        background: ${Z.Field};
        border-color: ${Z.Highlight};
      }
      ::slotted([role='combobox']:focus-within) {
        border-color: ${Z.Highlight};
        box-shadow: 0 0 0 1px ${Z.Highlight} inset;
      }
      ::slotted(input:placeholder) {
        color: ${Z.GrayText};
      }
    `))});class i5 extends K.PickerListItem{}let i6=i5.compose({baseName:"draft-picker-list-item",baseClass:K.PickerListItem,template:K.pickerListItemTemplate,styles:iX}),i3={jpAccordion:o7,jpAccordionItem:o9,jpAnchor:rh,jpAnchoredRegion:rg,jpAvatar:rx,jpBadge:rk,jpBreadcrumb:rS,jpBreadcrumbItem:rT,jpButton:rH,jpCard:rR,jpCheckbox:rG,jpCombobox:rU,jpDataGrid:r2,jpDataGridCell:rK,jpDataGridRow:r0,jpDateField:ao,jpDesignSystemProvider:ac,jpDialog:au,jpDisclosure:ab,jpDivider:av,jpListbox:ax,jpMenu:ak,jpMenuItem:aS,jpNumberField:aT,jpOption:aB,jpPicker:iZ,jpPickerList:i2,jpPickerListItem:i6,jpPickerMenu:iK,jpPickerMenuOption:i0,jpProgress:aN,jpProgressRing:aR,jpRadio:aG,jpRadioGroup:aq,jpSearch:aZ,jpSelect:aK,jpSkeleton:a1,jpSlider:a4,jpSliderLabel:io,jpSwitch:ii,jpTab:iu,jpTabPanel:ic,jpTabs:ib,jpTextArea:i$,jpTextField:iw,jpToolbar:ij,jpTooltip:iL,jpTreeItem:iM,jpTreeView:i_,register(e,...t){if(e)for(let o in this)"register"!==o&&this[o]().register(e,...t)}};function i4(e){return K.DesignSystem.getOrCreate(e).withPrefix("jp")}}}]);
//# sourceMappingURL=2282.cb634c4.js.map