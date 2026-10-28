
---
title: "JS逆向仓库001:某Q音乐JSVMP纯算逆向(中等)"
author: "Zsx"
pubDatetime: 2026-10-26T00:00:00+08:00
description: "JSVMP逆向"
tags:
  - JS逆向
  - WEB端
  - JSVMP
featured: false
draft: false
---
网址：aHR0cHM6Ly95LnFxLmNvbS8=

接口：aHR0cHM6Ly91Ni55LnFxLmNvbS9jZ2ktYmluL211c2ljcy5mY2c=

# 1.接口分析

随便搜索一首歌，点击播放，打开Devtools开发者工具抓包，如下图所示：

![1793003441989](image/a/1793003441989.png)

对比多个fcg接口，可以得知这个sign是变化的，所以说这个sign就是我们要逆向的参数，至于短横线就是一个13位的时间戳。
使用全局搜索大法，直接搜索sign。

![1793003580808](image/a/1793003580808.png)

可以很明显的看出sign是由u赋值的。

这个是一个switch case控制流，我们可以向上追溯u的生成。

![1793003705497](image/a/1793003705497.png)

可以很明显的发现：ie.getSecuritySign(r.data);其实就是u的生成。

这个是一个异步的方法调用，我们可以在控制台输入：

```
ie.getSecuritySign(r.data).then(i=>console.log(i));
```

通过.then方法，它会返回一个Promise的pending状态。

![1793003887725](image/a/1793003887725.png)

可以很明显的看到，u确实是ie.getSecuritySign(r.data)这个方法返回的值。

直接进入到这个方法内部，发现它是一个JSVMP。

![1793004024296](image/a/1793004024296.png)

直接把这整个JSVMP复制下来，可以看到：

```
((function () {
  var e = [];
  function t(e, t, n) {
    for (var r = [], i = 0; i++ < t; ) r.push((e += n));
    return r;
  }
  var n = t(0, 43, 0)
    .concat([62, 0, 62, 0, 63])
    .concat(t(51, 10, 1))
    .concat(t(0, 8, 0))
    .concat(t(0, 25, 1))
    .concat([0, 0, 0, 0, 63, 0])
    .concat(t(25, 26, 1));
  function r(e) {
    for (
      var t,
        r,
        i = String(e).replace(/[=]+$/, ""),
        o = i.length,
        a = 0,
        s = 0,
        u = [];
      s < o;
      s++
    )
      ~(r = n[i.charCodeAt(s)]) &&
        ((t = a % 4 ? 64 * t + r : r), a++ % 4) &&
        u.push(255 & (t >> ((-2 * a) & 6)));
    return u;
  }
  function i(e) {
    return (e >> 1) ^ -(1 & e);
  }
  var o = function (e) {
    for (
      var t = [],
        n = "undefined" != typeof Int8Array ? new Int8Array(r(e)) : r(e),
        o = n.length,
        a = 0;
      o > a;
    ) {
      var s = n[a++],
        u = 127 & s;
      s >= 0
        ? t.push(i(u))
        : ((u |= (127 & (s = n[a++])) << 7),
          s >= 0 ||
            ((u |= (127 & (s = n[a++])) << 14),
            s >= 0 ||
              ((u |= (127 & (s = n[a++])) << 21),
              s >= 0 || (u |= (s = n[a++]) << 28))),
          t.push(i(u)));
    }
    return t;
  };
  return function (t, n) {
    var r = o(t),
      i = function (t, n, o, a, s) {
        return function u() {
          for (
            var c,
              l,
              A,
              f = [o, a, n, this, arguments, u, r, 0],
              h = void 0,
              g = t,
              d = [];
            ;
          )
            try {
              for (;;)
                switch (r[++g]) {
                  case 0:
                    ((f[r[++g]] += String.fromCharCode(r[++g])),
                      (f[r[++g]] += String.fromCharCode(r[++g])),
                      (f[r[++g]] += String.fromCharCode(r[++g])));
                    break;
                  case 1:
                    ((f[r[++g]] += String.fromCharCode(r[++g])),
                      (f[r[++g]] += String.fromCharCode(r[++g])));
                    break;
                  case 2:
                    ((f[r[++g]] += String.fromCharCode(r[++g])),
                      (f[r[++g]] = f[r[++g]][f[r[++g]]]));
                    break;
                  case 3:
                    ((f[r[++g]] = f[r[++g]][f[r[++g]]]),
                      (f[r[++g]] = ""),
                      (f[r[++g]] += String.fromCharCode(r[++g])));
                    break;
                  case 4:
                    ((f[r[++g]] = f[r[++g]][r[++g]]),
                      (f[r[++g]] = ""),
                      (f[r[++g]] += String.fromCharCode(r[++g])));
                    break;
                  case 5:
                    ((f[r[++g]] += String.fromCharCode(r[++g])),
                      (f[r[++g]] = ""),
                      (f[r[++g]] += String.fromCharCode(r[++g])));
                    break;
                  case 6:
                    ((f[r[++g]][f[r[++g]]] = f[r[++g]]),
                      (f[r[++g]] = ""),
                      (f[r[++g]] += String.fromCharCode(r[++g])));
                    break;
                  case 7:
                    ((f[r[++g]][r[++g]] = f[r[++g]]),
                      (f[r[++g]] = r[++g]),
                      (f[r[++g]][r[++g]] = f[r[++g]]));
                    break;
                  case 8:
                    ((f[r[++g]] = ""),
                      (f[r[++g]] += String.fromCharCode(r[++g])));
                    break;
                  case 9:
                    for (
                      f[r[++g]] += String.fromCharCode(r[++g]),
                        l = [],
                        A = r[++g];
                      A > 0;
                      A--
                    )
                      l.push(f[r[++g]]);
                    f[r[++g]] = i(g + r[++g], l, o, a, s);
                    try {
                      Object.defineProperty(f[r[g - 1]], "length", {
                        value: r[++g],
                        configurable: !0,
                        writable: !1,
                        enumerable: !1,
                      });
                    } catch (e) {}
                    f[r[++g]] = f[r[++g]];
                    break;
                  case 10:
                    for (l = [], A = r[++g]; A > 0; A--) l.push(f[r[++g]]);
                    f[r[++g]] = i(g + r[++g], l, o, a, s);
                    try {
                      Object.defineProperty(f[r[g - 1]], "length", {
                        value: r[++g],
                        configurable: !0,
                        writable: !1,
                        enumerable: !1,
                      });
                    } catch (e) {}
                    ((f[r[++g]] = f[r[++g]]),
                      (f[r[++g]][f[r[++g]]] = f[r[++g]]));
                    break;
                  case 11:
                    ((f[r[++g]] = f[r[++g]][r[++g]]),
                      (f[r[++g]] = f[r[++g]][r[++g]]));
                    break;
                  case 12:
                    ((f[r[++g]] = f[r[++g]]),
                      (f[r[++g]][f[r[++g]]] = f[r[++g]]));
                    break;
                  case 13:
                    ((f[r[++g]] = f[r[++g]][f[r[++g]]]),
                      (f[r[++g]] = f[r[++g]][r[++g]]),
                      (f[r[++g]] = ""));
                    break;
                  case 14:
                    ((f[r[++g]] = f[r[++g]] == f[r[++g]]),
                      (f[r[++g]] = !f[r[++g]]),
                      (g += f[r[++g]] ? r[++g] : r[(++g, ++g)]));
                    break;
                  case 15:
                    ((f[r[++g]] = f[r[++g]][f[r[++g]]]),
                      (f[r[++g]] = typeof f[r[++g]]),
                      (f[r[++g]] = f[r[++g]] == f[r[++g]]));
                    break;
                  case 16:
                    ((f[r[++g]] = f[r[++g]][f[r[++g]]]),
                      (f[r[++g]] = f[r[++g]].call(f[r[++g]])));
                    break;
                  case 17:
                    ((f[r[++g]][f[r[++g]]] = f[r[++g]]),
                      (f[r[++g]] = f[r[++g]][r[++g]]),
                      (f[r[++g]] = ""));
                    break;
                  case 18:
                    ((f[r[++g]] = c),
                      (f[r[++g]] = f[r[++g]]),
                      d.push(g + r[++g]));
                    break;
                  case 19:
                    ((f[r[++g]] = typeof f[r[++g]]),
                      (f[r[++g]] = f[r[++g]] == f[r[++g]]),
                      (g += f[r[++g]] ? r[++g] : r[(++g, ++g)]));
                    break;
                  case 20:
                    ((f[r[++g]] = f[r[++g]][f[r[++g]]]),
                      (f[r[++g]] = typeof f[r[++g]]),
                      (f[r[++g]] = ""));
                    break;
                  case 21:
                    ((f[r[++g]] = f[r[++g]] === f[r[++g]]),
                      (f[r[++g]] = !f[r[++g]]),
                      (g += f[r[++g]] ? r[++g] : r[(++g, ++g)]));
                    break;
                  case 22:
                    ((f[r[++g]] = f[r[++g]] ^ f[r[++g]]),
                      (f[r[++g]] = f[r[++g]]),
                      (f[r[++g]] = f[r[++g]]));
                    break;
                  case 23:
                    f[r[++g]] = Array(r[++g]);
                    break;
                  case 24:
                    for (l = [], A = r[++g]; A > 0; A--) l.push(f[r[++g]]);
                    f[r[++g]] = i(g + r[++g], l, o, a, s);
                    try {
                      Object.defineProperty(f[r[g - 1]], "length", {
                        value: r[++g],
                        configurable: !0,
                        writable: !1,
                        enumerable: !1,
                      });
                    } catch (e) {}
                    break;
                  case 25:
                    f[r[++g]][r[++g]] = f[r[++g]];
                    break;
                  case 26:
                    d.push(g + r[++g]);
                    break;
                  case 27:
                    d.pop();
                    break;
                  case 28:
                    g += r[++g];
                    break;
                  case 29:
                    f[r[++g]] = c;
                    break;
                  case 30:
                    throw f[r[++g]];
                  case 31:
                    f[r[++g]] = "";
                    break;
                  case 32:
                    g += f[r[++g]] ? r[++g] : r[(++g, ++g)];
                    break;
                  case 33:
                    f[r[++g]] = f[r[++g]][f[r[++g]]];
                    break;
                  case 34:
                    f[r[++g]] = f[r[++g]][r[++g]];
                    break;
                  case 35:
                    f[r[++g]] = {};
                    break;
                  case 36:
                    f[r[++g]] = f[r[++g]];
                    break;
                  case 37:
                    f[r[++g]] = f[r[++g]].call(h, f[r[++g]]);
                    break;
                  case 38:
                    f[r[++g]] = f[r[++g]].call(h);
                    break;
                  case 39:
                    f[r[++g]] = typeof f[r[++g]];
                    break;
                  case 40:
                    f[r[++g]] += String.fromCharCode(r[++g]);
                    break;
                  case 41:
                    f[r[++g]][f[r[++g]]] = f[r[++g]];
                    break;
                  case 42:
                    f[r[++g]] = h;
                    break;
                  case 43:
                    return f[r[++g]];
                  case 44:
                    f[r[++g]] = f[r[++g]] === r[++g];
                    break;
                  case 45:
                    f[r[++g]] = r[++g];
                    break;
                  case 46:
                    f[r[++g]] = f[r[++g]] < f[r[++g]];
                    break;
                  case 47:
                    f[r[++g]] =
                      "bigint" == typeof f[r[g + 1]]
                        ? f[r[++g]]
                        : f[r[++g]] - 0;
                    break;
                  case 48:
                    f[r[++g]] = ++f[r[++g]];
                    break;
                  case 49:
                    f[r[++g]] = !f[r[++g]];
                    break;
                  case 50:
                    f[r[++g]] = f[r[++g]] in f[r[++g]];
                    break;
                  case 51:
                    f[r[++g]] = f[r[++g]].call(
                      f[r[++g]],
                      f[r[++g]],
                      f[r[++g]],
                      f[r[++g]],
                    );
                    break;
                  case 52:
                    f[r[++g]] = f[r[++g]].call(f[r[++g]], f[r[++g]]);
                    break;
                  case 53:
                    f[r[++g]] = new f[r[++g]](f[r[++g]]);
                    break;
                  case 54:
                    f[r[++g]] = f[r[++g]] + f[r[++g]];
                    break;
                  case 55:
                    f[r[++g]] = null;
                    break;
                  case 56:
                    f[r[++g]] = f[r[++g]] === f[r[++g]];
                    break;
                  case 57:
                    f[r[++g]] = f[r[++g]].call(h, f[r[++g]], f[r[++g]]);
                    break;
                  case 58:
                    f[r[++g]] = new f[r[++g]]();
                    break;
                  case 59:
                    f[r[++g]] = f[r[++g]].call(f[r[++g]], f[r[++g]], f[r[++g]]);
                    break;
                  case 60:
                    f[r[++g]] = f[r[++g]] / f[r[++g]];
                    break;
                  case 61:
                    f[r[++g]] = f[r[++g]] - f[r[++g]];
                    break;
                  case 62:
                    f[r[++g]] = -f[r[++g]];
                    break;
                  case 63:
                    f[r[++g]] = f[r[++g]] > r[++g];
                    break;
                  case 64:
                    f[r[++g]] = f[r[++g]] == f[r[++g]];
                    break;
                  case 65:
                    for (l = [], A = r[++g]; A > 0; A--) l.push(f[r[++g]]);
                    f[r[++g]] = f[r[++g]].apply(f[r[++g]], l);
                    break;
                  case 66:
                    f[r[++g]] = f[r[++g]] >>> r[++g];
                    break;
                  case 67:
                    f[r[++g]] = f[r[++g]] >> r[++g];
                    break;
                  case 68:
                    f[r[++g]] = f[r[++g]] * f[r[++g]];
                    break;
                  case 69:
                    f[r[++g]] = f[r[++g]] & r[++g];
                    break;
                  case 70:
                    f[r[++g]] = f[r[++g]] + r[++g];
                    break;
                  case 71:
                    f[r[++g]] = f[r[++g]] << r[++g];
                    break;
                  case 72:
                    f[r[++g]] = f[r[++g]] | f[r[++g]];
                    break;
                  case 73:
                    f[r[++g]] = f[r[++g]] ^ f[r[++g]];
                    break;
                  case 74:
                    f[r[++g]] = f[r[++g]] >= r[++g];
                    break;
                  case 75:
                    f[r[++g]] = f[r[++g]] | r[++g];
                    break;
                  case 76:
                    f[r[++g]] = f[r[++g]].call(f[r[++g]]);
                    break;
                  case 77:
                    f[r[++g]] = f[r[++g]] < r[++g];
                    break;
                  case 78:
                    f[r[++g]] = f[r[++g]] % f[r[++g]];
                    break;
                  case 79:
                    f[r[++g]] = f[r[++g]].call(
                      h,
                      f[r[++g]],
                      f[r[++g]],
                      f[r[++g]],
                    );
                    break;
                  case 80:
                    f[r[++g]] = new f[r[++g]](f[r[++g]], f[r[++g]]);
                }
            } catch (t) {
              if (
                (d.length > 0 && (e = []), (c = t), e.push(g), 0 === d.length)
              )
                throw s ? s(t, f, e) : t;
              ((g = d.pop()), e.pop());
            }
        };
      };
    return n ? void 0 : i;
  };
})()(
  "LhAALhIALhQALhYALhgALhoALhwALh4ALiAALiIALiQALiYALigALioALiwALi4ALjAALjIALjQALjYALjgALjoALjwALj4ALkAALkIALkQALkYALkgALkoALkwALk4ALlAALlIAMABehjQGMhAAXjAAXvo5AjISAF4wAF7COwIyFABeMABevD0CMhYAXjACFl6ETAAyGABeMAIWXvZRADIaAF40GjAAXqRXAjIcAF42OAo6XjxePl4AXswBXuoBXtwBAF7GAV7oAV7SAQJe3gFe3AE+ZgBmpgFm6gFm4AEAZuABZuQBZsoBAGbmAWbmAWbKAQBmyAFmigFm5AEAZuQBZt4BZuQBHmYAZmRmYl5kQGIGcj5iAGKmAWLqAWLgAQBi4AFi5AFiygEAYuYBYuYBYsoBAGLIAWKKAWLkAQBi5AFi3gFi5AFCYgBiMABo2lcCRGoeAEBqNiAwAGjAVwJEah4AQGocBkZkSGpkMh4AZDgCSmJoajACHGSQWQBMXmQyIABeMABe5KwBAExkXjIiAGQwAGTCsQEATF5kMiQAXjAAXvq8AQBMZF4yJgBkMABkmsgBAExeZDIoAF4wAF7w2wEATGReMioAZDAAZJLgAQBMXmQyLABeMABe/OMBAExkXjIuAGQwAhxknPoBAExeZDIwAF4wAF68gAIATGReMjIAZDACEmTwnQIATF5kMjQAXjACFF6EqwIATGReMjYAZDAAZMKwAgBMXmQyOABeMABelOkCAExkXjI6AGQwCjo4ICIyZPD/AgBMXmQyPABeMAQ6OF6UyAMATGReMj4AZDAgEB40NiAiMiQmKCosLjA8PmSM9QMATF5kMkAAXjAIQB48Pl6YrQQATGReMkIAZDAAZNC3BABMXmQyRABeMAREQl62ugQATGReMkYAZDACHGT+xAQATF5kMkgAXjAKRBgaSDZe2NMEAExkXjJKAGQwCkQYGkg2ZLDwBABMXmQyTABePl4AXsIBXuABXuABAF7YAV7SAV7GAQBewgFe6AFe0gEAXt4BXtwBXl4AXtQBXuYBXt4BAF7cAV52XsYBAF7QAV7CAV7kAQBe5gFeygFe6AEAXnpeqgFeqAEAXowBXlpecDJOAF4wBEROXrSRBQBMZF4yUABkMARQRGTCsgUATF5kMlIAXjAKREZKTFJe8McFAExkXkhUZERkRgA+XgBe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JD4oACjGASjkASjKAQAowgEo6AEoygEAKIoBKNgBKMoBACjaASjKASjcAQQo6AEmJCg+KAAoxgEowgEo3AEAKOwBKMIBKOYBaComJChIECo+KgAqzgEqygEq6AEAKoYBKt4BKtwBACroASrKASrwAQQq6AEoECo+KgAq7gEqygEqxAECKs4BKtgBaCwoECpALLABBj4qACrOASrKASroAQAqhgEq3gEq3AEAKugBKsoBKvABBCroASgQKj4qACrKASrwASrgAQAqygEq5AEq0gEAKtoBKsoBKtwBACroASrCASrYAQAqWiruASrKAQAqxAEqzgEq2AFoLCgQKkgSLEASJhRIEixAEhgGPioCKowBKooBVipIFBI+KgAqzgEqygEq6AEAKooBKvABKugBACrKASrcASrmAQAq0gEq3gEq3AFCKBQqPioAKq4BKooBKoQBACqOASqYASq+AQAqyAEqygEqxAEAKuoBKs4BKr4BACrkASrKASrcAQAqyAEqygEq5AEAKsoBKuQBKr4BACrSASrcASrMAVAq3gFoJigUKkgWJkAWoAIGPiYAJs4BJsoBJugBACagASbCASbkAQAmwgEm2gEmygEAJugBJsoBJuQBQioUJj4oACikASiKASicAQAoiAEoigEopAECKIoBKKQBQiQUKGgoKhQkSBgoQigUJj4mACasASaKASacAQAmiAEmngEmpAFCJBQmaCYoFCRIGiY+Jj4kACTGASTeASTcAQAkxgEkwgEk6AEGKCYkKir8AXZIKCYaKkIqSCRoJCpIGFYkPiQAJM4BJMoBJOgBACSgASTCASTkAQAkwgEk2gEkygEAJOgBJMoBJOQBQioUJD5IAEiqAUicAUiaAQBIggFIpgFIlgEASIoBSIgBSL4BAEisAUiKAUicAQBIiAFIngFIpAEASL4BSK4BSIoBAEiEAUiOAUiYAUIoFkhoSCoUKEgcSEJIFCQ+JAAkqgEknAEkmgEAJIIBJKYBJJYBACSKASSIASS+AQAkpAEkigEknAEAJIgBJIoBJKQBACSKASSkASS+AQAkrgEkigEkhAECJI4BJJgBQigWJGgkSBQoSB4kPiQ+KAAoxgEo3gEo3AEAKMYBKMIBKOgBBkgkKCoq/AF2JkgkHCpCKiYoaCgqJh5WKCQoIigUPigCKKoBKIoBVig6KDwoFhQIABAE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",
  !1,
)(
  -1,
  [],
  {
    get SuppressedError() {
      return "undefined" == typeof SuppressedError ? void 0 : SuppressedError;
    },
    get globalThis() {
      return "undefined" == typeof globalThis ? void 0 : globalThis;
    },
    get window() {
      return "undefined" == typeof window ? void 0 : window;
    },
    get self() {
      return "undefined" == typeof self ? void 0 : self;
    },
    get Array() {
      return "undefined" == typeof Array ? void 0 : Array;
    },
    get Uint8Array() {
      return "undefined" == typeof Uint8Array ? void 0 : Uint8Array;
    },
    get String() {
      return "undefined" == typeof String ? void 0 : String;
    },
    get Promise() {
      return "undefined" == typeof Promise ? void 0 : Promise;
    },
    get document() {
      return "undefined" == typeof document ? void 0 : document;
    },
    get RegExp() {
      return "undefined" == typeof RegExp ? void 0 : RegExp;
    },
    get TextEncoder() {
      return "undefined" == typeof TextEncoder ? void 0 : TextEncoder;
    },
    get TextDecoder() {
      return "undefined" == typeof TextDecoder ? void 0 : TextDecoder;
    },
    get crypto() {
      return "undefined" == typeof crypto ? void 0 : crypto;
    },
    get Symbol() {
      return "undefined" == typeof Symbol ? void 0 : Symbol;
    },
    get navigator() {
      return "undefined" == typeof navigator ? void 0 : navigator;
    },
    get Date() {
      return "undefined" == typeof Date ? void 0 : Date;
    },
    get Intl() {
      return "undefined" == typeof Intl ? void 0 : Intl;
    },
    get screen() {
      return "undefined" == typeof screen ? void 0 : screen;
    },
    get Float32Array() {
      return "undefined" == typeof Float32Array ? void 0 : Float32Array;
    },
    get matchMedia() {
      return "undefined" == typeof matchMedia ? void 0 : matchMedia;
    },
    get Function() {
      return "undefined" == typeof Function ? void 0 : Function;
    },
    get Object() {
      return "undefined" == typeof Object ? void 0 : Object;
    },
    get btoa() {
      return "undefined" == typeof btoa ? void 0 : btoa;
    },
    get Math() {
      return "undefined" == typeof Math ? void 0 : Math;
    },
    get parseInt() {
      return "undefined" == typeof parseInt ? void 0 : parseInt;
    },
    get JSON() {
      return "undefined" == typeof JSON ? void 0 : JSON;
    },
    get location() {
      return "undefined" == typeof location ? void 0 : location;
    },
    get Blob() {
      return "undefined" == typeof Blob ? void 0 : Blob;
    },
    get fetch() {
      return "undefined" == typeof fetch ? void 0 : fetch;
    },
  },
  [
    void 0,
    null,
    3432918353,
    3864292196,
    2869860233,
    2716044179,
    1444728091,
    2530024501,
    2246822507,
    3266489909,
    3735928559,
  ],
  void 0,
)(),
  ("undefined" !== typeof globalThis
    ? globalThis
    : "undefined" !== typeof window
      ? window
      : "undefined" !== typeof self
        ? self
        : void 0
  ).__TmeWebSec_U,
  ("undefined" !== typeof globalThis
    ? globalThis
    : "undefined" !== typeof window
      ? window
      : "undefined" !== typeof self
        ? self
        : void 0
  ).__TmeWebSec_I,
  ("undefined" !== typeof globalThis
    ? globalThis
    : "undefined" !== typeof window
      ? window
      : "undefined" !== typeof self
        ? self
        : void 0
  ).__TmeWebSec_M,
  ("undefined" !== typeof globalThis
    ? globalThis
    : "undefined" !== typeof window
      ? window
      : "undefined" !== typeof self
        ? self
        : void 0
  ).__TmeWebSec_x);
const ne = (
  "undefined" !== typeof globalThis
    ? globalThis
    : "undefined" !== typeof window
      ? window
      : "undefined" !== typeof self
        ? self
        : void 0
).__TmeWebSec_D;
(("undefined" !== typeof globalThis
  ? globalThis
  : "undefined" !== typeof window
    ? window
    : "undefined" !== typeof self
      ? self
      : void 0
).__TmeWebSec_fingerprint,
  ("undefined" !== typeof globalThis
    ? globalThis
    : "undefined" !== typeof window
      ? window
      : "undefined" !== typeof self
        ? self
        : void 0
  ).__TmeWebSec_report);
const re = (
    "undefined" !== typeof globalThis
      ? globalThis
      : "undefined" !== typeof window
        ? window
        : "undefined" !== typeof self
          ? self
          : void 0
  ).__TmeWebSec_seccgi,
  ie = (
    "undefined" !== typeof globalThis
      ? globalThis
      : "undefined" !== typeof window
        ? window
        : "undefined" !== typeof self
          ? self
          : void 0
  ).__TmeWebSec_sign;
```

这个其实就是算出sign的JSVMP了。最底下有一个：

```
ie = (
    "undefined" !== typeof globalThis
      ? globalThis
      : "undefined" !== typeof window
        ? window
        : "undefined" !== typeof self
          ? self
          : void 0
  ).__TmeWebSec_sign;

该JSVMP样本为2026.10.26的版本.
```
我们可以通过调用ie.getSecuritySign()方法拿到一个sign的测试值。

```
ie.getSecuritySign('12345').then(i=>console.log(i));
// 会输出：zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca
```

现在这个JSVMP已经跑起来了，不过现在拿到的值肯定是假的值。

我们下一步还需要对这个JSVMP进行插桩，通过看log日志的方法分析这个VMP的来龙去脉。

# 2.VMP插桩

这个VMP的特征其实非常明显，它是一个栈式虚拟机。

我们可以先通过在VMP的解释器处，对call、apply处进行插桩分析。

ctrl+f搜索一下，call+apply一共10处调用。

把这10处都插上桩。

# 3.插桩代码参考
```
const { log } = require('console');
const { inspect } = require('node:util');
const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('node:fs');
const dom = new JSDOM('', {
    url: "https://example.com/",
    pretendToBeVisual: true,
    virtualConsole: new VirtualConsole(),
    // runScripts: "outside-only"
});
const window = dom.window;

const logConfig = {
    common: true,
    opCode: true,
    promise: true
}

let __seq = 0
let __logSeq = 0
let __pendingConcat = null; // Pending "+=" log aggregation.

function __inspectValue(value) {
    try {
        return inspect(value, {
            depth: 3,
            breakLength: Infinity,
            compact: true,
            maxArrayLength: 64,
            maxStringLength: 500,
            getters: false,
        });
    } catch (error) {
        return `<uninspectable: ${error && error.message || error}>`;
    }
}

function __inspectArgs(args) {
    if (!Array.isArray(args)) return __inspectValue(args);
    const values = args.map(function (value) {
        return value === window ? "window" : __inspectValue(value);
    });
    return "[" + values.join(", ") + "]";
}

function __functionName(func) {
    if (typeof func !== "function") {
        return __inspectValue(func);
    }
    try {
        if (func.name) return func.name;
    } catch {}
    try {
        const source = Function.prototype.toString.call(func);
        const match =
            source.match(/^\s*(?:async\s+)?function\s+([^\s(]+)/) ||
            source.match(/^\s*(?:async\s*)?([^\s(=]+)\s*\(/);
        if (match && match[1]) return match[1];
    } catch {}
    return "<anonymous>";
}

function __isPromiseLike(value) {
    if (
        value === null ||
        (typeof value !== "object" && typeof value !== "function")
    ) {
        return false;
    }
    try {
        return typeof value.then === "function";
    } catch {
        return false;
    }
}

function flushPendingConcat() {
    if (!__pendingConcat) return;
    const pending = __pendingConcat;
    __pendingConcat = null;
    log("seq:", ++__logSeq, "id:", pending.id, "运算符:", "+=", "args:", JSON.stringify(pending.args), "res:", JSON.stringify(pending.res));
}

function prevLog(func, t, args) {
    flushPendingConcat();
    if (!logConfig.common) return;
    const id = ++__seq;
    const thisText = t === window ? "window" : __inspectValue(t);
    log("seq:", ++__logSeq, "id:", id, "func:", func, "this:", thisText, "args:", __inspectArgs(args));
    return {id, func};
}

function nextLog(id, func, res, state) {
    flushPendingConcat();
    if (!logConfig.common) return;
    if (state) {
        log("seq:", ++__logSeq, "id:", id, "func:", func, "state:", state, "res:", __inspectValue(res));
    } else {
        log("seq:", ++__logSeq, "id:", id, "func:", func, "res:", __inspectValue(res));
    }
    return res;
}

function observePromise(id, func, promise) {
    if (!logConfig.common || !logConfig.promise || !__isPromiseLike(promise)) return;
    Promise.resolve(promise).then(
        function (value) {
            nextLog(id, func, value, "fulfilled");
        },
        function (reason) {
            nextLog(id, func, reason, "rejected");
        },
    );
}

function __traceVmInvoke(opcode, func, thisArg, args) {
    const funcName = __functionName(func);
    const ctx = prevLog(opcode + ":" + funcName, thisArg, args);
    const res =
        opcode === "apply"
            ? func.apply(thisArg, args)
            : func.call(thisArg, ...args);
    const pending = __isPromiseLike(res);
    if (ctx) {
        nextLog(ctx.id, ctx.func, res, pending ? "pending" : undefined);
    }
    if (pending && ctx) {
        observePromise(ctx.id, ctx.func, res);
    }
    return res;
}

function prevOpCode(opcode, args) {
    if (!logConfig.opCode) return;
    if (opcode !== "+=") flushPendingConcat();
    const id = ++__seq;
    return { id, opcode, args };
}

function nextOpCode(ctx, res) {
    if (!logConfig.opCode) return res;
    if (ctx.opcode === "+=") {
        if (__pendingConcat && __pendingConcat.res === ctx.args[0]) {
            __pendingConcat.args[1] += ctx.args[1];
            __pendingConcat.res = res;
            __pendingConcat.count++;
        } else {
            flushPendingConcat();
            __pendingConcat = {
                id: ctx.id,
                args: [ctx.args[0], ctx.args[1]],
                res,
                count: 1,
            };
        }
        return res;
    }
    flushPendingConcat();
    log("seq:", ++__logSeq, "id:", ctx.id, "运算符:", ctx.opcode, "args:", JSON.stringify(ctx.args), "res:", JSON.stringify(res));
    return res;
}
```

# 4.call,apply处插桩日志分析
对JSVMP解释器的call,apply处插桩

在终端输入:**node.exe a.js > vm.log 2>&1**
日志会被保存到vm.log文件中,方便分析

插桩日志:
```
seq: 1 id: 1 func: call:u this: undefined args: [{}]
seq: 2 id: 1 func: call:u res: undefined
seq: 3 id: 2 func: call:u this: undefined args: []
seq: 4 id: 2 func: call:u res: { [Function: u] o: [Function: u], v: [Function: u], p: [Function: u], h: [Function: u], l: [Function: u], T: [Function: u], m: [Function: u], _: [Function: u], U: [Function: u], S: [Function: u], F: [Function: u], A: [Function: u], M: [Function: u], j: [Function: u], P: [Function: u], I: [Function: u] }
seq: 5 id: 3 func: call:u this: undefined args: []
seq: 6 id: 3 func: call:u res: { [Function: u] D: [Function: u] }
seq: 7 id: 4 func: call:u this: undefined args: []
seq: 8 id: 4 func: call:u res: { [Function: u] C: [Function: u] }
seq: 9 id: 5 func: call:u this: undefined args: []
seq: 10 id: 5 func: call:u res: { [Function: u] q: [Function: u] }
seq: 11 id: 6 func: call:u this: undefined args: []
seq: 12 id: 6 func: call:u res: { [Function: u] R: [Function: u], '$': [Function: u] }
seq: 13 id: 7 func: call:u this: undefined args: []
seq: 14 id: 7 func: call:u res: { [Function: u] k: [Function: u] }
seq: 15 id: 8 func: call:u this: undefined args: []
seq: 16 id: 8 func: call:u res: { [Function: u] N: [Function: u] }
seq: 17 id: 9 func: call:u this: undefined args: []
seq: 18 id: 9 func: call:u res: { [Function: u] O: [Function: u] }
seq: 19 id: 10 func: call:u this: undefined args: []
seq: 20 id: 10 func: call:u res: { [Function: u] B: [Function: u] }
seq: 21 id: 11 func: call:u this: undefined args: []
seq: 22 id: 11 func: call:u res: { [Function: u] M: [Function: u], K: [Function: u], L: [Function: u], G: [Function: u] }
seq: 23 id: 12 func: call:u this: undefined args: []
seq: 24 id: 12 func: call:u res: { [Function: u] getInstance: [Function: u] }
seq: 25 id: 13 func: call:u this: undefined args: []
seq: 26 id: 13 func: call:u res: { [Function: u] getInstance: [Function: u] }
seq: 27 id: 14 func: call:u this: undefined args: []
seq: 28 id: 14 func: call:u res: { [Function: u] X: [Function: u], Y: [Function: u], Z: [Function: u], nn: [Function: u], V: [Function: u] }
seq: 29 id: 15 func: call:u this: undefined args: []
seq: 30 id: 15 func: call:u res: { [Function: u] get: [Function: u], set: [Function: u], remove: [Function: u] }
seq: 31 id: 16 func: call:u this: undefined args: []
seq: 32 id: 16 func: call:u res: { [Function: u] getInstance: [Function: u], gn: [Function: u], hn: [Function: u], an: '_tme_did', Un: 365, sn: '|||', yn: 'secid', pn: 1, wn: 4, En: 'T$m3_S3c_2024!xK9' }
seq: 33 id: 17 func: call:u this: undefined args: []
seq: 34 id: 17 func: call:u res: { [Function: u] getInstance: [Function: u], jn: [Function: u], hn: [Function: u], Pn: [Function: u], In: [Function: u], an: '_tme_cid', Un: 365, yn: 'cid', pn: 1, wn: 4, En: 'T$m3_S3c_2024!xK9', Dn: 0 }
seq: 35 id: 18 func: call:u this: undefined args: []
seq: 36 id: 18 func: call:u res: { [Function: u] Cn: [Function: u], Nn: [Function: u], Wn: { Hn: 'T0', Xn: 'T1', Zn: 'T2', Qn: 'T3', Vn: 'T4', Yn: 'T5', nt: 'T6', tt: 'T7', rt: 'T8', et: 'T9', it: 'T10', ut: 'T11', ot: 'T12', ft: 'T13', ct: 'T14', dt: 'T15', vt: 'T16', st: 'T17', yt: 'T18', ht: 'T19', gt: 'T20', wt: 'T100', lt: 'T101', Et: 'T102', Tt: 'T103', _t: 'T104', Ut: 'T105', St: 'T106', bt: 'T122', Ft: 'T124', At: 'T200', xt: 'T201' }, qn: [ 138, 61, 226, 151 ], Rn: [ 91, 199, 20, 248 ], '$n': [ 105, 163, 208, 78 ], kn: [ 39, 159, 60, 178 ], On: [ 241, 93, 139, 35 ], Bn: [ 166, 55, 206, 72 ], Kn: [ 146, 122, 229, 27 ], Ln: [ 60, 132, 111, 217 ] }
seq: 37 id: 19 func: call:u this: undefined args: []
seq: 38 id: 19 func: call:u res: [Function: u]
seq: 39 id: 20 func: call:u this: undefined args: []
seq: 40 id: 20 func: call:u res: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' }
seq: 41 id: 21 func: call:u this: undefined args: []
seq: 42 id: 21 func: call:u res: { [Function: u] getInstance: [Function: u], kt: 'FingerprintModule' }
seq: 43 id: 22 func: call:u this: undefined args: []
seq: 44 id: 22 func: call:u res: { [Function: u] Ot: [Function: u], Bt: [ 'qq.com', 'joox.com', 'tencentmusic.com', 'wavecommittee.com', 'kugou.com', 'kuwo.cn' ] }
seq: 45 id: 23 func: call:u this: undefined args: []
seq: 46 id: 23 func: call:u res: { [Function: u] getInstance: [Function: u], kt: 'SignModule' }
seq: 47 id: 24 func: call:u this: undefined args: []
seq: 48 id: 24 func: call:u res: { [Function: u] getInstance: [Function: u], kt: 'SecCgiModule' }
seq: 49 id: 25 func: call:u this: undefined args: []
seq: 50 id: 25 func: call:u res: { [Function: u] Kt: [Function: u], Lt: [Function: u] }
seq: 51 id: 26 func: call:u this: undefined args: []
seq: 52 id: 26 func: call:u res: { [Function: u] getInstance: [Function: u], Jt: 'https://t.y.qq.com/cgi-bin/musicu.fcg' }
seq: 53 id: 27 func: call:u this: undefined args: []
seq: 54 id: 27 func: call:u res: { [Function: u] getInstance: [Function: u], Wt: [Function: u], kt: 'TMESec', isInitialized: false }
seq: 55 id: 28 func: call:u this: { [Function: u] getInstance: [Function: u], kt: 'FingerprintModule' } args: []
seq: 56 id: 29 func: call:u this: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' } args: ['FingerprintModule', 'Fingerprint 模块初始化中...']
seq: 57 id: 29 func: call:u res: undefined
seq: 58 id: 30 func: call:u this: u { Mt: '', jt: -1, Pt: -1, It: false, Dt: '1' } args: []
seq: 59 id: 30 func: call:u res: undefined
seq: 60 id: 31 func: call:u this: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' } args: ['FingerprintModule', 'Fingerprint 模块初始化成功']
seq: 61 id: 31 func: call:u res: undefined
seq: 62 id: 28 func: call:u res: u { version: '0.0.1', Nt: u { Mt: '', jt: -1, Pt: -1, It: true, Dt: '1' } }
seq: 63 id: 32 func: call:u this: { [Function: u] getInstance: [Function: u], kt: 'SignModule' } args: []
seq: 64 id: 33 func: call:u this: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' } args: ['SignModule', 'Sign 模块初始化中...']
seq: 65 id: 33 func: call:u res: undefined
seq: 66 id: 32 func: call:u res: u { version: '0.0.1' }
seq: 67 id: 34 func: call:u this: { [Function: u] getInstance: [Function: u], kt: 'SecCgiModule' } args: []
seq: 68 id: 35 func: call:u this: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' } args: ['SecCgiModule', 'SecCgi 模块初始化中...']
seq: 69 id: 35 func: call:u res: undefined
seq: 70 id: 34 func: call:u res: u { version: '0.0.1' }
seq: 71 id: 36 func: call:u this: { [Function: u] getInstance: [Function: u], Jt: 'https://t.y.qq.com/cgi-bin/musicu.fcg' } args: []
seq: 72 id: 37 func: call:u this: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' } args: ['ReportModule', 'Report 模块初始化中...']
seq: 73 id: 37 func: call:u res: undefined
seq: 74 id: 36 func: call:u res: u { transport: u {}, Gt: null }
seq: 75 id: 38 func: call:u this: undefined args: []
seq: 76 id: 39 func: call:function this: undefined args: [true]
seq: 77 id: 39 func: call:function res: undefined
seq: 78 id: 38 func: call:u state: pending res: Promise { true }
seq: 79 id: 40 func: call:u this: undefined args: []
seq: 80 id: 41 func: call:function this: undefined args: [true]
seq: 81 id: 41 func: call:function res: undefined
seq: 82 id: 40 func: call:u state: pending res: Promise { true }
seq: 83 id: 42 func: call:all this: [Function: Promise] args: [[ Promise { true }, Promise { true } ]]
seq: 84 id: 42 func: call:all state: pending res: Promise { <pending> }
seq: 85 id: 43 func: call:then this: Promise { <pending> } args: [[Function: u]]
seq: 86 id: 43 func: call:then state: pending res: Promise { <pending> }
seq: 87 id: 38 func: call:u state: fulfilled res: true
seq: 88 id: 40 func: call:u state: fulfilled res: true
seq: 89 id: 42 func: call:all state: fulfilled res: [ true, true ]
seq: 90 id: 44 func: call:encode this: { encoding: 'utf-8' } args: ['12345']
seq: 91 id: 44 func: call:encode res: Uint8Array(5) [ 49, 50, 51, 52, 53 ]
seq: 92 id: 45 func: call:digest this: SubtleCrypto {} args: ['SHA-1', Uint8Array(5) [ 49, 50, 51, 52, 53 ]]
seq: 93 id: 45 func: call:digest state: pending res: Promise { <pending> }
seq: 94 id: 46 func: call:then this: Promise { <pending> } args: [[Function: u]]
seq: 95 id: 46 func: call:then state: pending res: Promise { <pending> }
seq: 96 id: 45 func: call:digest state: fulfilled res: ArrayBuffer { [Uint8Contents]: <8c b2 23 7d 06 79 ca 88 db 64 64 ea c6 0d a9 63 45 51 39 64>, [byteLength]: 20 }
seq: 97 id: 47 func: call:u this: { [Function: u] Ot: [Function: u], Bt: [ 'qq.com', 'joox.com', 'tencentmusic.com', 'wavecommittee.com', 'kugou.com', 'kuwo.cn' ] } args: []
seq: 98 id: 48 func: call:u this: undefined args: [window]
seq: 99 id: 48 func: call:u res: 'object'
seq: 100 id: 49 func: call:u this: undefined args: [Navigator {}]
seq: 101 id: 49 func: call:u res: 'object'
seq: 102 id: 47 func: call:u res: 'FE'
seq: 103 id: 50 func: call:map this: [ 3, 1, 6, 17 ] args: [[Function: u]]
seq: 104 id: 51 func: call:toString this: 6 args: [16]
seq: 105 id: 51 func: call:toString res: '6'
seq: 106 id: 52 func: call:padStart this: '6' args: [2, '0']
seq: 107 id: 52 func: call:padStart res: '06'
seq: 108 id: 53 func: call:toString this: 35 args: [16]
seq: 109 id: 53 func: call:toString res: '23'
seq: 110 id: 54 func: call:padStart this: '23' args: [2, '0']
seq: 111 id: 54 func: call:padStart res: '23'
seq: 112 id: 55 func: call:toString this: 136 args: [16]
seq: 113 id: 55 func: call:toString res: '88'
seq: 114 id: 56 func: call:padStart this: '88' args: [2, '0']
seq: 115 id: 56 func: call:padStart res: '88'
seq: 116 id: 57 func: call:toString this: 57 args: [16]
seq: 117 id: 57 func: call:toString res: '39'
seq: 118 id: 58 func: call:padStart this: '39' args: [2, '0']
seq: 119 id: 58 func: call:padStart res: '39'
seq: 120 id: 50 func: call:map res: [ '06', '23', '88', '39' ]
seq: 121 id: 59 func: call:join this: [ '06', '23', '88', '39' ] args: ['']
seq: 122 id: 59 func: call:join res: '06238839'
seq: 123 id: 60 func: call:map this: [ 16, 12, 8, 5 ] args: [[Function: u]]
seq: 124 id: 61 func: call:toString this: 81 args: [16]
seq: 125 id: 61 func: call:toString res: '51'
seq: 126 id: 62 func: call:padStart this: '51' args: [2, '0']
seq: 127 id: 62 func: call:padStart res: '51'
seq: 128 id: 63 func: call:toString this: 13 args: [16]
seq: 129 id: 63 func: call:toString res: 'd'
seq: 130 id: 64 func: call:padStart this: 'd' args: [2, '0']
seq: 131 id: 64 func: call:padStart res: '0d'
seq: 132 id: 65 func: call:toString this: 100 args: [16]
seq: 133 id: 65 func: call:toString res: '64'
seq: 134 id: 66 func: call:padStart this: '64' args: [2, '0']
seq: 135 id: 66 func: call:padStart res: '64'
seq: 136 id: 67 func: call:toString this: 202 args: [16]
seq: 137 id: 67 func: call:toString res: 'ca'
seq: 138 id: 68 func: call:padStart this: 'ca' args: [2, '0']
seq: 139 id: 68 func: call:padStart res: 'ca'
seq: 140 id: 60 func: call:map res: [ '51', '0d', '64', 'ca' ]
seq: 141 id: 69 func: call:join this: [ '51', '0d', '64', 'ca' ] args: ['']
seq: 142 id: 69 func: call:join res: '510d64ca'
seq: 143 id: 70 func: call:u this: { [Function: u] getInstance: [Function: u] } args: []
seq: 144 id: 70 func: call:u res: u {}
seq: 145 id: 71 func: call:u this: u {} args: [Uint8Array(20) [ 25, 192, 181, 206, 60, 92, 96, 119, 190, 114, 207, 118, 73, 4, 19, 65, 26, 157, 224, 119 ]]
seq: 146 id: 72 func: call:u this: undefined args: [Uint8Array(20) [ 25, 192, 181, 206, 60, 92, 96, 119, 190, 114, 207, 118, 73, 4, 19, 65, 26, 157, 224, 119 ]]
seq: 147 id: 73 func: call:fromCharCode this: [Function: String] args: [25]
seq: 148 id: 73 func: call:fromCharCode res: '\x19'
seq: 149 id: 74 func: call:fromCharCode this: [Function: String] args: [192]
seq: 150 id: 74 func: call:fromCharCode res: 'À'
seq: 151 id: 75 func: call:fromCharCode this: [Function: String] args: [181]
seq: 152 id: 75 func: call:fromCharCode res: 'µ'
seq: 153 id: 76 func: call:fromCharCode this: [Function: String] args: [206]
seq: 154 id: 76 func: call:fromCharCode res: 'Î'
seq: 155 id: 77 func: call:fromCharCode this: [Function: String] args: [60]
seq: 156 id: 77 func: call:fromCharCode res: '<'
seq: 157 id: 78 func: call:fromCharCode this: [Function: String] args: [92]
seq: 158 id: 78 func: call:fromCharCode res: '\\'
seq: 159 id: 79 func: call:fromCharCode this: [Function: String] args: [96]
seq: 160 id: 79 func: call:fromCharCode res: '`'
seq: 161 id: 80 func: call:fromCharCode this: [Function: String] args: [119]
seq: 162 id: 80 func: call:fromCharCode res: 'w'
seq: 163 id: 81 func: call:fromCharCode this: [Function: String] args: [190]
seq: 164 id: 81 func: call:fromCharCode res: '¾'
seq: 165 id: 82 func: call:fromCharCode this: [Function: String] args: [114]
seq: 166 id: 82 func: call:fromCharCode res: 'r'
seq: 167 id: 83 func: call:fromCharCode this: [Function: String] args: [207]
seq: 168 id: 83 func: call:fromCharCode res: 'Ï'
seq: 169 id: 84 func: call:fromCharCode this: [Function: String] args: [118]
seq: 170 id: 84 func: call:fromCharCode res: 'v'
seq: 171 id: 85 func: call:fromCharCode this: [Function: String] args: [73]
seq: 172 id: 85 func: call:fromCharCode res: 'I'
seq: 173 id: 86 func: call:fromCharCode this: [Function: String] args: [4]
seq: 174 id: 86 func: call:fromCharCode res: '\x04'
seq: 175 id: 87 func: call:fromCharCode this: [Function: String] args: [19]
seq: 176 id: 87 func: call:fromCharCode res: '\x13'
seq: 177 id: 88 func: call:fromCharCode this: [Function: String] args: [65]
seq: 178 id: 88 func: call:fromCharCode res: 'A'
seq: 179 id: 89 func: call:fromCharCode this: [Function: String] args: [26]
seq: 180 id: 89 func: call:fromCharCode res: '\x1A'
seq: 181 id: 90 func: call:fromCharCode this: [Function: String] args: [157]
seq: 182 id: 90 func: call:fromCharCode res: '\x9D'
seq: 183 id: 91 func: call:fromCharCode this: [Function: String] args: [224]
seq: 184 id: 91 func: call:fromCharCode res: 'à'
seq: 185 id: 92 func: call:fromCharCode this: [Function: String] args: [119]
seq: 186 id: 92 func: call:fromCharCode res: 'w'
seq: 187 id: 72 func: call:u res: '\x19ÀµÎ<\\`w¾rÏvI\x04\x13A\x1A\x9Dàw'
seq: 188 id: 93 func: call:btoa this: undefined args: ['\x19ÀµÎ<\\`w¾rÏvI\x04\x13A\x1A\x9Dàw']
seq: 189 id: 93 func: call:btoa res: 'GcC1zjxcYHe+cs92SQQTQRqd4Hc='
seq: 190 id: 71 func: call:u res: { H: true, data: 'GcC1zjxcYHe+cs92SQQTQRqd4Hc=' }
seq: 191 id: 94 func: call:toLowerCase this: 'GcC1zjxcYHe+cs92SQQTQRqd4Hc=' args: []
seq: 192 id: 94 func: call:toLowerCase res: 'gcc1zjxcyhe+cs92sqqtqrqd4hc='
seq: 193 id: 95 func: call:RegExp this: undefined args: ['=+$', '']
seq: 194 id: 95 func: call:RegExp res: /=+$/
seq: 195 id: 96 func: call:replace this: 'gcc1zjxcyhe+cs92sqqtqrqd4hc=' args: [/=+$/, '']
seq: 196 id: 96 func: call:replace res: 'gcc1zjxcyhe+cs92sqqtqrqd4hc'
seq: 197 id: 97 func: call:RegExp this: undefined args: ['[\\/+]', 'g']
seq: 198 id: 97 func: call:RegExp res: /[\/+]/g
seq: 199 id: 98 func: call:replace this: 'gcc1zjxcyhe+cs92sqqtqrqd4hc' args: [/[\/+]/g, '']
seq: 200 id: 98 func: call:replace res: 'gcc1zjxcyhecs92sqqtqrqd4hc'
seq: 201 id: 46 func: call:then state: fulfilled res: 'zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca'
seq: 202 id: 43 func: call:then state: fulfilled res: 'zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca'
zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca
```
日志非常少,200行,非常方便观察分析.

这里最后的**zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca**其实就是sign值.当前现在的sign值是假值,因为没有过环境检测,走的是错误的JSVMP分支.这个我们后续再说,先进行分析.

首先我先说下,sign其实由4部分组成:
**固定前缀:zzc + 开头段 + 中间段 +结尾段**

# 5.中间段生成
我们这里先看中间段,从日志最底部开始分析.

```
seq: 145 id: 71 func: call:u this: u {} args: [Uint8Array(20) [ 25, 192, 181, 206, 60, 92, 96, 119, 190, 114, 207, 118, 73, 4, 19, 65, 26, 157, 224, 119 ]]
seq: 146 id: 72 func: call:u this: undefined args: [Uint8Array(20) [ 25, 192, 181, 206, 60, 92, 96, 119, 190, 114, 207, 118, 73, 4, 19, 65, 26, 157, 224, 119 ]]
seq: 147 id: 73 func: call:fromCharCode this: [Function: String] args: [25]
seq: 148 id: 73 func: call:fromCharCode res: '\x19'
seq: 149 id: 74 func: call:fromCharCode this: [Function: String] args: [192]
seq: 150 id: 74 func: call:fromCharCode res: 'À'
seq: 151 id: 75 func: call:fromCharCode this: [Function: String] args: [181]
seq: 152 id: 75 func: call:fromCharCode res: 'µ'
seq: 153 id: 76 func: call:fromCharCode this: [Function: String] args: [206]
seq: 154 id: 76 func: call:fromCharCode res: 'Î'
seq: 155 id: 77 func: call:fromCharCode this: [Function: String] args: [60]
seq: 156 id: 77 func: call:fromCharCode res: '<'
seq: 157 id: 78 func: call:fromCharCode this: [Function: String] args: [92]
seq: 158 id: 78 func: call:fromCharCode res: '\\'
seq: 159 id: 79 func: call:fromCharCode this: [Function: String] args: [96]
seq: 160 id: 79 func: call:fromCharCode res: '`'
seq: 161 id: 80 func: call:fromCharCode this: [Function: String] args: [119]
seq: 162 id: 80 func: call:fromCharCode res: 'w'
seq: 163 id: 81 func: call:fromCharCode this: [Function: String] args: [190]
seq: 164 id: 81 func: call:fromCharCode res: '¾'
seq: 165 id: 82 func: call:fromCharCode this: [Function: String] args: [114]
seq: 166 id: 82 func: call:fromCharCode res: 'r'
seq: 167 id: 83 func: call:fromCharCode this: [Function: String] args: [207]
seq: 168 id: 83 func: call:fromCharCode res: 'Ï'
seq: 169 id: 84 func: call:fromCharCode this: [Function: String] args: [118]
seq: 170 id: 84 func: call:fromCharCode res: 'v'
seq: 171 id: 85 func: call:fromCharCode this: [Function: String] args: [73]
seq: 172 id: 85 func: call:fromCharCode res: 'I'
seq: 173 id: 86 func: call:fromCharCode this: [Function: String] args: [4]
seq: 174 id: 86 func: call:fromCharCode res: '\x04'
seq: 175 id: 87 func: call:fromCharCode this: [Function: String] args: [19]
seq: 176 id: 87 func: call:fromCharCode res: '\x13'
seq: 177 id: 88 func: call:fromCharCode this: [Function: String] args: [65]
seq: 178 id: 88 func: call:fromCharCode res: 'A'
seq: 179 id: 89 func: call:fromCharCode this: [Function: String] args: [26]
seq: 180 id: 89 func: call:fromCharCode res: '\x1A'
seq: 181 id: 90 func: call:fromCharCode this: [Function: String] args: [157]
seq: 182 id: 90 func: call:fromCharCode res: '\x9D'
seq: 183 id: 91 func: call:fromCharCode this: [Function: String] args: [224]
seq: 184 id: 91 func: call:fromCharCode res: 'à'
seq: 185 id: 92 func: call:fromCharCode this: [Function: String] args: [119]
seq: 186 id: 92 func: call:fromCharCode res: 'w'
seq: 187 id: 72 func: call:u res: '\x19ÀµÎ<\\`w¾rÏvI\x04\x13A\x1A\x9Dàw'
seq: 188 id: 93 func: call:btoa this: undefined args: ['\x19ÀµÎ<\\`w¾rÏvI\x04\x13A\x1A\x9Dàw']
seq: 189 id: 93 func: call:btoa res: 'GcC1zjxcYHe+cs92SQQTQRqd4Hc='
seq: 190 id: 71 func: call:u res: { H: true, data: 'GcC1zjxcYHe+cs92SQQTQRqd4Hc=' }
seq: 191 id: 94 func: call:toLowerCase this: 'GcC1zjxcYHe+cs92SQQTQRqd4Hc=' args: []
seq: 192 id: 94 func: call:toLowerCase res: 'gcc1zjxcyhe+cs92sqqtqrqd4hc='
seq: 193 id: 95 func: call:RegExp this: undefined args: ['=+$', '']
seq: 194 id: 95 func: call:RegExp res: /=+$/
seq: 195 id: 96 func: call:replace this: 'gcc1zjxcyhe+cs92sqqtqrqd4hc=' args: [/=+$/, '']
seq: 196 id: 96 func: call:replace res: 'gcc1zjxcyhe+cs92sqqtqrqd4hc'
seq: 197 id: 97 func: call:RegExp this: undefined args: ['[\\/+]', 'g']
seq: 198 id: 97 func: call:RegExp res: /[\/+]/g
seq: 199 id: 98 func: call:replace this: 'gcc1zjxcyhe+cs92sqqtqrqd4hc' args: [/[\/+]/g, '']
seq: 200 id: 98 func: call:replace res: 'gcc1zjxcyhecs92sqqtqrqd4hc'
seq: 201 id: 46 func: call:then state: fulfilled res: 'zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca'
seq: 202 id: 43 func: call:then state: fulfilled res: 'zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca'
zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca
```
注意这里,这个部分我们可以知道sign值的最后一部中间段怎么来的.

首先是一个20位长度的列表:[ 25, 192, 181, 206, 60, 92, 96, 119, 190, 114, 207, 118, 73, 4, 19, 65, 26, 157, 224, 119 ],对列表中的每一个元素做fromCharCode运算,然后join到一起,得到一长串鬼画符,然后通过btoa(一长串鬼画符)来得到**GcC1zjxcYHe+cs92SQQTQRqd4Hc=**字符串.

再通过两轮RegExp正则,替换掉字符串中的特殊符号,最终得到了中间段**gcc1zjxcyhecs92sqqtqrqd4hc**

# 6.开头段,结尾段生成
```
seq: 103 id: 50 func: call:map this: [ 3, 1, 6, 17 ] args: [[Function: u]]
seq: 104 id: 51 func: call:toString this: 6 args: [16]
seq: 105 id: 51 func: call:toString res: '6'
seq: 106 id: 52 func: call:padStart this: '6' args: [2, '0']
seq: 107 id: 52 func: call:padStart res: '06'
seq: 108 id: 53 func: call:toString this: 35 args: [16]
seq: 109 id: 53 func: call:toString res: '23'
seq: 110 id: 54 func: call:padStart this: '23' args: [2, '0']
seq: 111 id: 54 func: call:padStart res: '23'
seq: 112 id: 55 func: call:toString this: 136 args: [16]
seq: 113 id: 55 func: call:toString res: '88'
seq: 114 id: 56 func: call:padStart this: '88' args: [2, '0']
seq: 115 id: 56 func: call:padStart res: '88'
seq: 116 id: 57 func: call:toString this: 57 args: [16]
seq: 117 id: 57 func: call:toString res: '39'
seq: 118 id: 58 func: call:padStart this: '39' args: [2, '0']
seq: 119 id: 58 func: call:padStart res: '39'
seq: 120 id: 50 func: call:map res: [ '06', '23', '88', '39' ]
seq: 121 id: 59 func: call:join this: [ '06', '23', '88', '39' ] args: ['']
seq: 122 id: 59 func: call:join res: '06238839'
seq: 123 id: 60 func: call:map this: [ 16, 12, 8, 5 ] args: [[Function: u]]
seq: 124 id: 61 func: call:toString this: 81 args: [16]
seq: 125 id: 61 func: call:toString res: '51'
seq: 126 id: 62 func: call:padStart this: '51' args: [2, '0']
seq: 127 id: 62 func: call:padStart res: '51'
seq: 128 id: 63 func: call:toString this: 13 args: [16]
seq: 129 id: 63 func: call:toString res: 'd'
seq: 130 id: 64 func: call:padStart this: 'd' args: [2, '0']
seq: 131 id: 64 func: call:padStart res: '0d'
seq: 132 id: 65 func: call:toString this: 100 args: [16]
seq: 133 id: 65 func: call:toString res: '64'
seq: 134 id: 66 func: call:padStart this: '64' args: [2, '0']
seq: 135 id: 66 func: call:padStart res: '64'
seq: 136 id: 67 func: call:toString this: 202 args: [16]
seq: 137 id: 67 func: call:toString res: 'ca'
seq: 138 id: 68 func: call:padStart this: 'ca' args: [2, '0']
seq: 139 id: 68 func: call:padStart res: 'ca'
seq: 140 id: 60 func: call:map res: [ '51', '0d', '64', 'ca' ]
seq: 141 id: 69 func: call:join this: [ '51', '0d', '64', 'ca' ] args: ['']
seq: 142 id: 69 func: call:join res: '510d64ca'
```

这部分其实也好分析,仔细观察一下,其实是对两组4个长度的列表里面的元素分别转16进制hex然后toString转字符串,然后再对它们补0
如果不需要补0就保持不变.

最终得出了两组16进制hex的列表,最后再对各自的列表join字符串得到**开头段06238839和结尾段510d64ca**

重复运行VMP我们会发现最开始的三个字符zzc是保持不变的,这个就是**固定前缀**

现在我们已经知道所有部分的字符串的来源了,现在只需要解决的是两个问题.

1.中间段:开头的20位数组[ 25, 192, 181, 206, 60, 92, 96, 119, 190, 114, 207, 118, 73, 4, 19, 65, 26, 157, 224, 119 ]是怎么来的
2.开头段和结尾段:两组4个长度的列表是怎么来的.

我们再观察一下日志:
```
seq: 90 id: 44 func: call:encode this: { encoding: 'utf-8' } args: ['12345']
seq: 91 id: 44 func: call:encode res: Uint8Array(5) [ 49, 50, 51, 52, 53 ]
seq: 92 id: 45 func: call:digest this: SubtleCrypto {} args: ['SHA-1', Uint8Array(5) [ 49, 50, 51, 52, 53 ]]
seq: 93 id: 45 func: call:digest state: pending res: Promise { <pending> }
seq: 94 id: 46 func: call:then this: Promise { <pending> } args: [[Function: u]]
seq: 95 id: 46 func: call:then state: pending res: Promise { <pending> }
seq: 96 id: 45 func: call:digest state: fulfilled res: ArrayBuffer { [Uint8Contents]: <8c b2 23 7d 06 79 ca 88 db 64 64 ea c6 0d a9 63 45 51 39 64>, [byteLength]: 20 }
seq: 97 id: 47 func: call:u this: { [Function: u] Ot: [Function: u], Bt: [ 'qq.com', 'joox.com', 'tencentmusic.com', 'wavecommittee.com', 'kugou.com', 'kuwo.cn' ] } args: []
seq: 98 id: 48 func: call:u this: undefined args: [window]
seq: 99 id: 48 func: call:u res: 'object'
seq: 100 id: 49 func: call:u this: undefined args: [Navigator {}]
seq: 101 id: 49 func: call:u res: 'object'
seq: 102 id: 47 func: call:u res: 'FE'
seq: 103 id: 50 func: call:map this: [ 3, 1, 6, 17 ] args: [[Function: u]]
seq: 104 id: 51 func: call:toString this: 6 args: [16]
seq: 105 id: 51 func: call:toString res: '6'
seq: 106 id: 52 func: call:padStart this: '6' args: [2, '0']
seq: 107 id: 52 func: call:padStart res: '06'
seq: 108 id: 53 func: call:toString this: 35 args: [16]
seq: 109 id: 53 func: call:toString res: '23'
seq: 110 id: 54 func: call:padStart this: '23' args: [2, '0']
seq: 111 id: 54 func: call:padStart res: '23'
seq: 112 id: 55 func: call:toString this: 136 args: [16]
seq: 113 id: 55 func: call:toString res: '88'
seq: 114 id: 56 func: call:padStart this: '88' args: [2, '0']
seq: 115 id: 56 func: call:padStart res: '88'
seq: 116 id: 57 func: call:toString this: 57 args: [16]
seq: 117 id: 57 func: call:toString res: '39'
seq: 118 id: 58 func: call:padStart this: '39' args: [2, '0']
seq: 119 id: 58 func: call:padStart res: '39'
seq: 120 id: 50 func: call:map res: [ '06', '23', '88', '39' ]
seq: 121 id: 59 func: call:join this: [ '06', '23', '88', '39' ] args: ['']
seq: 122 id: 59 func: call:join res: '06238839'
seq: 123 id: 60 func: call:map this: [ 16, 12, 8, 5 ] args: [[Function: u]]
seq: 124 id: 61 func: call:toString this: 81 args: [16]
seq: 125 id: 61 func: call:toString res: '51'
seq: 126 id: 62 func: call:padStart this: '51' args: [2, '0']
seq: 127 id: 62 func: call:padStart res: '51'
seq: 128 id: 63 func: call:toString this: 13 args: [16]
seq: 129 id: 63 func: call:toString res: 'd'
seq: 130 id: 64 func: call:padStart this: 'd' args: [2, '0']
seq: 131 id: 64 func: call:padStart res: '0d'
seq: 132 id: 65 func: call:toString this: 100 args: [16]
seq: 133 id: 65 func: call:toString res: '64'
seq: 134 id: 66 func: call:padStart this: '64' args: [2, '0']
seq: 135 id: 66 func: call:padStart res: '64'
seq: 136 id: 67 func: call:toString this: 202 args: [16]
seq: 137 id: 67 func: call:toString res: 'ca'
seq: 138 id: 68 func: call:padStart this: 'ca' args: [2, '0']
seq: 139 id: 68 func: call:padStart res: 'ca'
seq: 140 id: 60 func: call:map res: [ '51', '0d', '64', 'ca' ]
seq: 141 id: 69 func: call:join this: [ '51', '0d', '64', 'ca' ] args: ['']
seq: 142 id: 69 func: call:join res: '510d64ca'
```

我们这里vmp测试的是:**ie.getSecuritySign('12345').then(i=>console.log(i));**
传入的字符串是"12345"

在这段日志的开头部分我们可以发现:
```
seq: 90 id: 44 func: call:encode this: { encoding: 'utf-8' } args: ['12345']
seq: 91 id: 44 func: call:encode res: Uint8Array(5) [ 49, 50, 51, 52, 53 ]
seq: 92 id: 45 func: call:digest this: SubtleCrypto {} args: ['SHA-1', Uint8Array(5) [ 49, 50, 51, 52, 53 ]]
seq: 93 id: 45 func: call:digest state: pending res: Promise { <pending> }
seq: 94 id: 46 func: call:then this: Promise { <pending> } args: [[Function: u]]
seq: 95 id: 46 func: call:then state: pending res: Promise { <pending> }
seq: 96 id: 45 func: call:digest state: fulfilled res: ArrayBuffer { [Uint8Contents]: <8c b2 23 7d 06 79 ca 88 db 64 64 ea c6 0d a9 63 45 51 39 64>, [byteLength]: 20 }
```

他是通过调用sha1处理传入的字符串的,最后得到**<8c b2 23 7d 06 79 ca 88 db 64 64 ea c6 0d a9 63 45 51 39 64>**
这个是20个字节,也就是40位16进制hex

我们首先要怀疑它是不是标准sha1,有没要魔改.我们可以自己测试一下.
这里我测过了,就是标准sha1,并没有出现魔改.

然后我们可以发现开头段和结尾段都有map出现:
```
seq: 103 id: 50 func: call:map this: [ 3, 1, 6, 17 ] args: [[Function: u]]
seq: 123 id: 60 func: call:map this: [ 16, 12, 8, 5 ] args: [[Function: u]]
```

有没要可能这个其实就是对**<8c b2 23 7d 06 79 ca 88 db 64 64 ea c6 0d a9 63 45 51 39 64>**取下标索引呢?
日志里出现的this值:[06,23,88,39],[81,13,100,202]

我们可以测试一下,发现这里实际上的索引是:[ 4, 2, 7, 18 ], [ 17, 13, 9, 6 ] !!!!!
也就是[ 3, 1, 6, 17 ],[ 16, 12, 8, 5 ] 每一个元素 + 1 !

这里我就直接说了,这里是一个**检测点**

JSVMP会检测当前的运行环境,如果它发现环境不对,就会走错误的分支,索引选择器全部+1,生成错误的开头段和结尾段

真正的真值走的索引是[ 3, 1, 6, 17 ],[ 16, 12, 8, 5 ].

也就是说:开头段 = SHA1("输入的字符串")得出的20字节数组再取下标索引[ 3, 1, 6, 17 ]; 结尾段 = SHA1("输入的字符串")得出的20字节数组再取下标索引[ 16, 12, 8, 5 ]

现在的话开头段和结尾段我们知道了.


总结一下现在的情况:

1.中间段:开头的20位数组是怎么来的 (待解决)
2.开头段和结尾段:两组4个长度的列表是怎么来的. (已解决)
3.VMP环境检测:错误的环境导致错误的索引选择器 (待解决)


# 7.20位数组生成(位运算符插桩)
接下来我们就是要解决20位数组和VMP环境检测的问题,我们先看20位数组.

既然call,apply插桩插完了,那我们自然要对位运算符之类的地方进行插桩了.
继续把桩都插满.其实这里插桩的话,一般就是三种方法:

1.手动插(太麻烦)
2.AST提取节点自动插桩(这个AI能力不强的时候可以古法插桩)
3.AI自动插桩(我一般都是把插桩代码弄好,然后直接让ai插桩就可以，非常方便)

插完位运算符后的日志:
```
seq: 1 id: 1 func: call:u this: undefined args: [{}]
seq: 2 id: 1 func: call:u res: undefined
seq: 3 id: 2 func: call:u this: undefined args: []
seq: 4 id: 2 func: call:u res: { [Function: u] o: [Function: u], v: [Function: u], p: [Function: u], h: [Function: u], l: [Function: u], T: [Function: u], m: [Function: u], _: [Function: u], U: [Function: u], S: [Function: u], F: [Function: u], A: [Function: u], M: [Function: u], j: [Function: u], P: [Function: u], I: [Function: u] }
seq: 5 id: 3 func: call:u this: undefined args: []
seq: 6 id: 3 func: call:u res: { [Function: u] D: [Function: u] }
seq: 7 id: 4 func: call:u this: undefined args: []
seq: 8 id: 4 func: call:u res: { [Function: u] C: [Function: u] }
seq: 9 id: 5 func: call:u this: undefined args: []
seq: 10 id: 5 func: call:u res: { [Function: u] q: [Function: u] }
seq: 11 id: 6 func: call:u this: undefined args: []
seq: 12 id: 6 func: call:u res: { [Function: u] R: [Function: u], '$': [Function: u] }
seq: 13 id: 7 func: call:u this: undefined args: []
seq: 14 id: 7 func: call:u res: { [Function: u] k: [Function: u] }
seq: 15 id: 8 func: call:u this: undefined args: []
seq: 16 id: 8 func: call:u res: { [Function: u] N: [Function: u] }
seq: 17 id: 9 func: call:u this: undefined args: []
seq: 18 id: 9 func: call:u res: { [Function: u] O: [Function: u] }
seq: 19 id: 10 func: call:u this: undefined args: []
seq: 20 id: 10 func: call:u res: { [Function: u] B: [Function: u] }
seq: 21 id: 11 func: call:u this: undefined args: []
seq: 22 id: 11 func: call:u res: { [Function: u] M: [Function: u], K: [Function: u], L: [Function: u], G: [Function: u] }
seq: 23 id: 12 func: call:u this: undefined args: []
seq: 24 id: 12 func: call:u res: { [Function: u] getInstance: [Function: u] }
seq: 25 id: 13 func: call:u this: undefined args: []
seq: 26 id: 13 func: call:u res: { [Function: u] getInstance: [Function: u] }
seq: 27 id: 14 func: call:u this: undefined args: []
seq: 28 id: 14 func: call:u res: { [Function: u] X: [Function: u], Y: [Function: u], Z: [Function: u], nn: [Function: u], V: [Function: u] }
seq: 29 id: 15 func: call:u this: undefined args: []
seq: 30 id: 15 func: call:u res: { [Function: u] get: [Function: u], set: [Function: u], remove: [Function: u] }
seq: 31 id: 16 func: call:u this: undefined args: []
seq: 32 id: 16 func: call:u res: { [Function: u] getInstance: [Function: u], gn: [Function: u], hn: [Function: u], an: '_tme_did', Un: 365, sn: '|||', yn: 'secid', pn: 1, wn: 4, En: 'T$m3_S3c_2024!xK9' }
seq: 33 id: 17 func: call:u this: undefined args: []
seq: 34 id: 17 func: call:u res: { [Function: u] getInstance: [Function: u], jn: [Function: u], hn: [Function: u], Pn: [Function: u], In: [Function: u], an: '_tme_cid', Un: 365, yn: 'cid', pn: 1, wn: 4, En: 'T$m3_S3c_2024!xK9', Dn: 0 }
seq: 35 id: 18 func: call:u this: undefined args: []
seq: 36 id: 18 func: call:u res: { [Function: u] Cn: [Function: u], Nn: [Function: u], Wn: { Hn: 'T0', Xn: 'T1', Zn: 'T2', Qn: 'T3', Vn: 'T4', Yn: 'T5', nt: 'T6', tt: 'T7', rt: 'T8', et: 'T9', it: 'T10', ut: 'T11', ot: 'T12', ft: 'T13', ct: 'T14', dt: 'T15', vt: 'T16', st: 'T17', yt: 'T18', ht: 'T19', gt: 'T20', wt: 'T100', lt: 'T101', Et: 'T102', Tt: 'T103', _t: 'T104', Ut: 'T105', St: 'T106', bt: 'T122', Ft: 'T124', At: 'T200', xt: 'T201' }, qn: [ 138, 61, 226, 151 ], Rn: [ 91, 199, 20, 248 ], '$n': [ 105, 163, 208, 78 ], kn: [ 39, 159, 60, 178 ], On: [ 241, 93, 139, 35 ], Bn: [ 166, 55, 206, 72 ], Kn: [ 146, 122, 229, 27 ], Ln: [ 60, 132, 111, 217 ] }
seq: 37 id: 19 func: call:u this: undefined args: []
seq: 38 id: 19 func: call:u res: [Function: u]
seq: 39 id: 20 func: call:u this: undefined args: []
seq: 40 id: 20 func: call:u res: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' }
seq: 41 id: 21 func: call:u this: undefined args: []
seq: 42 id: 21 func: call:u res: { [Function: u] getInstance: [Function: u], kt: 'FingerprintModule' }
seq: 43 id: 22 func: call:u this: undefined args: []
seq: 44 id: 22 func: call:u res: { [Function: u] Ot: [Function: u], Bt: [ 'qq.com', 'joox.com', 'tencentmusic.com', 'wavecommittee.com', 'kugou.com', 'kuwo.cn' ] }
seq: 45 id: 23 func: call:u this: undefined args: []
seq: 46 id: 23 func: call:u res: { [Function: u] getInstance: [Function: u], kt: 'SignModule' }
seq: 47 id: 24 func: call:u this: undefined args: []
seq: 48 id: 24 func: call:u res: { [Function: u] getInstance: [Function: u], kt: 'SecCgiModule' }
seq: 49 id: 25 func: call:u this: undefined args: []
seq: 50 id: 25 func: call:u res: { [Function: u] Kt: [Function: u], Lt: [Function: u] }
seq: 51 id: 26 func: call:u this: undefined args: []
seq: 52 id: 26 func: call:u res: { [Function: u] getInstance: [Function: u], Jt: 'https://t.y.qq.com/cgi-bin/musicu.fcg' }
seq: 53 id: 27 func: call:u this: undefined args: []
seq: 54 id: 27 func: call:u res: { [Function: u] getInstance: [Function: u], Wt: [Function: u], kt: 'TMESec', isInitialized: false }
seq: 55 id: 28 func: call:u this: { [Function: u] getInstance: [Function: u], kt: 'FingerprintModule' } args: []
seq: 56 id: 29 func: call:u this: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' } args: ['FingerprintModule', 'Fingerprint 模块初始化中...']
seq: 57 id: 29 func: call:u res: undefined
seq: 58 id: 30 func: call:u this: u { Mt: '', jt: -1, Pt: -1, It: false, Dt: '1' } args: []
seq: 59 id: 30 func: call:u res: undefined
seq: 60 id: 31 func: call:u this: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' } args: ['FingerprintModule', 'Fingerprint 模块初始化成功']
seq: 61 id: 31 func: call:u res: undefined
seq: 62 id: 28 func: call:u res: u { version: '0.0.1', Nt: u { Mt: '', jt: -1, Pt: -1, It: true, Dt: '1' } }
seq: 63 id: 32 func: call:u this: { [Function: u] getInstance: [Function: u], kt: 'SignModule' } args: []
seq: 64 id: 33 func: call:u this: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' } args: ['SignModule', 'Sign 模块初始化中...']
seq: 65 id: 33 func: call:u res: undefined
seq: 66 id: 32 func: call:u res: u { version: '0.0.1' }
seq: 67 id: 34 func: call:u this: { [Function: u] getInstance: [Function: u], kt: 'SecCgiModule' } args: []
seq: 68 id: 35 func: call:u this: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' } args: ['SecCgiModule', 'SecCgi 模块初始化中...']
seq: 69 id: 35 func: call:u res: undefined
seq: 70 id: 34 func: call:u res: u { version: '0.0.1' }
seq: 71 id: 36 func: call:u this: { [Function: u] getInstance: [Function: u], Jt: 'https://t.y.qq.com/cgi-bin/musicu.fcg' } args: []
seq: 72 id: 37 func: call:u this: { [Function: u] qt: [Function: u], d: [Function: u], Rt: [Function: u], w: [Function: u], e: [Function: u], level: 0, '$t': '[TMESec]' } args: ['ReportModule', 'Report 模块初始化中...']
seq: 73 id: 37 func: call:u res: undefined
seq: 74 id: 36 func: call:u res: u { transport: u {}, Gt: null }
seq: 75 id: 38 func: call:u this: undefined args: []
seq: 76 id: 39 func: call:function this: undefined args: [true]
seq: 77 id: 39 func: call:function res: undefined
seq: 78 id: 38 func: call:u state: pending res: Promise { true }
seq: 79 id: 40 func: call:u this: undefined args: []
seq: 80 id: 41 func: call:function this: undefined args: [true]
seq: 81 id: 41 func: call:function res: undefined
seq: 82 id: 40 func: call:u state: pending res: Promise { true }
seq: 83 id: 42 func: call:all this: [Function: Promise] args: [[ Promise { true }, Promise { true } ]]
seq: 84 id: 42 func: call:all state: pending res: Promise { <pending> }
seq: 85 id: 43 func: call:then this: Promise { <pending> } args: [[Function: u]]
seq: 86 id: 43 func: call:then state: pending res: Promise { <pending> }
seq: 87 id: 38 func: call:u state: fulfilled res: true
seq: 88 id: 40 func: call:u state: fulfilled res: true
seq: 89 id: 42 func: call:all state: fulfilled res: [ true, true ]
seq: 90 id: 44 func: call:encode this: { encoding: 'utf-8' } args: ['12345']
seq: 91 id: 44 func: call:encode res: Uint8Array(5) [ 49, 50, 51, 52, 53 ]
seq: 92 id: 45 func: call:digest this: SubtleCrypto {} args: ['SHA-1', Uint8Array(5) [ 49, 50, 51, 52, 53 ]]
seq: 93 id: 45 func: call:digest state: pending res: Promise { <pending> }
seq: 94 id: 46 func: call:then this: Promise { <pending> } args: [[Function: u]]
seq: 95 id: 46 func: call:then state: pending res: Promise { <pending> }
seq: 96 id: 45 func: call:digest state: fulfilled res: ArrayBuffer { [Uint8Contents]: <8c b2 23 7d 06 79 ca 88 db 64 64 ea c6 0d a9 63 45 51 39 64>, [byteLength]: 20 }
seq: 97 id: 47 func: call:u this: { [Function: u] Ot: [Function: u], Bt: [ 'qq.com', 'joox.com', 'tencentmusic.com', 'wavecommittee.com', 'kugou.com', 'kuwo.cn' ] } args: []
seq: 98 id: 48 func: call:u this: undefined args: [window]
seq: 99 id: 48 func: call:u res: 'object'
seq: 100 id: 49 func: call:u this: undefined args: [Navigator {}]
seq: 101 id: 49 func: call:u res: 'object'
seq: 102 id: 47 func: call:u res: 'FE'
seq: 103 id: 50 运算符: ^ args: [140,149] res: 25
seq: 104 id: 51 运算符: ^ args: [178,114] res: 192
seq: 105 id: 52 运算符: ^ args: [35,150] res: 181
seq: 106 id: 53 运算符: ^ args: [125,179] res: 206
seq: 107 id: 54 运算符: ^ args: [6,58] res: 60
seq: 108 id: 55 运算符: ^ args: [121,37] res: 92
seq: 109 id: 56 运算符: ^ args: [202,170] res: 96
seq: 110 id: 57 运算符: ^ args: [136,255] res: 119
seq: 111 id: 58 运算符: ^ args: [219,101] res: 190
seq: 112 id: 59 运算符: ^ args: [100,22] res: 114
seq: 113 id: 60 运算符: ^ args: [100,171] res: 207
seq: 114 id: 61 运算符: ^ args: [234,156] res: 118
seq: 115 id: 62 运算符: ^ args: [198,143] res: 73
seq: 116 id: 63 运算符: ^ args: [13,9] res: 4
seq: 117 id: 64 运算符: ^ args: [169,186] res: 19
seq: 118 id: 65 运算符: ^ args: [99,34] res: 65
seq: 119 id: 66 运算符: ^ args: [69,95] res: 26
seq: 120 id: 67 运算符: ^ args: [81,204] res: 157
seq: 121 id: 68 运算符: ^ args: [57,217] res: 224
seq: 122 id: 69 运算符: ^ args: [100,19] res: 119
seq: 123 id: 70 func: call:map this: [ 3, 1, 6, 17 ] args: [[Function: u]]
seq: 124 id: 71 func: call:toString this: 6 args: [16]
seq: 125 id: 71 func: call:toString res: '6'
seq: 126 id: 72 func: call:padStart this: '6' args: [2, '0']
seq: 127 id: 72 func: call:padStart res: '06'
seq: 128 id: 73 func: call:toString this: 35 args: [16]
seq: 129 id: 73 func: call:toString res: '23'
seq: 130 id: 74 func: call:padStart this: '23' args: [2, '0']
seq: 131 id: 74 func: call:padStart res: '23'
seq: 132 id: 75 func: call:toString this: 136 args: [16]
seq: 133 id: 75 func: call:toString res: '88'
seq: 134 id: 76 func: call:padStart this: '88' args: [2, '0']
seq: 135 id: 76 func: call:padStart res: '88'
seq: 136 id: 77 func: call:toString this: 57 args: [16]
seq: 137 id: 77 func: call:toString res: '39'
seq: 138 id: 78 func: call:padStart this: '39' args: [2, '0']
seq: 139 id: 78 func: call:padStart res: '39'
seq: 140 id: 70 func: call:map res: [ '06', '23', '88', '39' ]
seq: 141 id: 79 func: call:join this: [ '06', '23', '88', '39' ] args: ['']
seq: 142 id: 79 func: call:join res: '06238839'
seq: 143 id: 80 func: call:map this: [ 16, 12, 8, 5 ] args: [[Function: u]]
seq: 144 id: 81 func: call:toString this: 81 args: [16]
seq: 145 id: 81 func: call:toString res: '51'
seq: 146 id: 82 func: call:padStart this: '51' args: [2, '0']
seq: 147 id: 82 func: call:padStart res: '51'
seq: 148 id: 83 func: call:toString this: 13 args: [16]
seq: 149 id: 83 func: call:toString res: 'd'
seq: 150 id: 84 func: call:padStart this: 'd' args: [2, '0']
seq: 151 id: 84 func: call:padStart res: '0d'
seq: 152 id: 85 func: call:toString this: 100 args: [16]
seq: 153 id: 85 func: call:toString res: '64'
seq: 154 id: 86 func: call:padStart this: '64' args: [2, '0']
seq: 155 id: 86 func: call:padStart res: '64'
seq: 156 id: 87 func: call:toString this: 202 args: [16]
seq: 157 id: 87 func: call:toString res: 'ca'
seq: 158 id: 88 func: call:padStart this: 'ca' args: [2, '0']
seq: 159 id: 88 func: call:padStart res: 'ca'
seq: 160 id: 80 func: call:map res: [ '51', '0d', '64', 'ca' ]
seq: 161 id: 89 func: call:join this: [ '51', '0d', '64', 'ca' ] args: ['']
seq: 162 id: 89 func: call:join res: '510d64ca'
seq: 163 id: 90 func: call:u this: { [Function: u] getInstance: [Function: u] } args: []
seq: 164 id: 90 func: call:u res: u {}
seq: 165 id: 91 func: call:u this: u {} args: [Uint8Array(20) [ 25, 192, 181, 206, 60, 92, 96, 119, 190, 114, 207, 118, 73, 4, 19, 65, 26, 157, 224, 119 ]]
seq: 166 id: 92 func: call:u this: undefined args: [Uint8Array(20) [ 25, 192, 181, 206, 60, 92, 96, 119, 190, 114, 207, 118, 73, 4, 19, 65, 26, 157, 224, 119 ]]
seq: 167 id: 93 func: call:fromCharCode this: [Function: String] args: [25]
seq: 168 id: 93 func: call:fromCharCode res: '\x19'
seq: 169 id: 94 func: call:fromCharCode this: [Function: String] args: [192]
seq: 170 id: 94 func: call:fromCharCode res: 'À'
seq: 171 id: 95 func: call:fromCharCode this: [Function: String] args: [181]
seq: 172 id: 95 func: call:fromCharCode res: 'µ'
seq: 173 id: 96 func: call:fromCharCode this: [Function: String] args: [206]
seq: 174 id: 96 func: call:fromCharCode res: 'Î'
seq: 175 id: 97 func: call:fromCharCode this: [Function: String] args: [60]
seq: 176 id: 97 func: call:fromCharCode res: '<'
seq: 177 id: 98 func: call:fromCharCode this: [Function: String] args: [92]
seq: 178 id: 98 func: call:fromCharCode res: '\\'
seq: 179 id: 99 func: call:fromCharCode this: [Function: String] args: [96]
seq: 180 id: 99 func: call:fromCharCode res: '`'
seq: 181 id: 100 func: call:fromCharCode this: [Function: String] args: [119]
seq: 182 id: 100 func: call:fromCharCode res: 'w'
seq: 183 id: 101 func: call:fromCharCode this: [Function: String] args: [190]
seq: 184 id: 101 func: call:fromCharCode res: '¾'
seq: 185 id: 102 func: call:fromCharCode this: [Function: String] args: [114]
seq: 186 id: 102 func: call:fromCharCode res: 'r'
seq: 187 id: 103 func: call:fromCharCode this: [Function: String] args: [207]
seq: 188 id: 103 func: call:fromCharCode res: 'Ï'
seq: 189 id: 104 func: call:fromCharCode this: [Function: String] args: [118]
seq: 190 id: 104 func: call:fromCharCode res: 'v'
seq: 191 id: 105 func: call:fromCharCode this: [Function: String] args: [73]
seq: 192 id: 105 func: call:fromCharCode res: 'I'
seq: 193 id: 106 func: call:fromCharCode this: [Function: String] args: [4]
seq: 194 id: 106 func: call:fromCharCode res: '\x04'
seq: 195 id: 107 func: call:fromCharCode this: [Function: String] args: [19]
seq: 196 id: 107 func: call:fromCharCode res: '\x13'
seq: 197 id: 108 func: call:fromCharCode this: [Function: String] args: [65]
seq: 198 id: 108 func: call:fromCharCode res: 'A'
seq: 199 id: 109 func: call:fromCharCode this: [Function: String] args: [26]
seq: 200 id: 109 func: call:fromCharCode res: '\x1A'
seq: 201 id: 110 func: call:fromCharCode this: [Function: String] args: [157]
seq: 202 id: 110 func: call:fromCharCode res: '\x9D'
seq: 203 id: 111 func: call:fromCharCode this: [Function: String] args: [224]
seq: 204 id: 111 func: call:fromCharCode res: 'à'
seq: 205 id: 112 func: call:fromCharCode this: [Function: String] args: [119]
seq: 206 id: 112 func: call:fromCharCode res: 'w'
seq: 207 id: 92 func: call:u res: '\x19ÀµÎ<\\`w¾rÏvI\x04\x13A\x1A\x9Dàw'
seq: 208 id: 113 func: call:btoa this: undefined args: ['\x19ÀµÎ<\\`w¾rÏvI\x04\x13A\x1A\x9Dàw']
seq: 209 id: 113 func: call:btoa res: 'GcC1zjxcYHe+cs92SQQTQRqd4Hc='
seq: 210 id: 91 func: call:u res: { H: true, data: 'GcC1zjxcYHe+cs92SQQTQRqd4Hc=' }
seq: 211 id: 114 func: call:toLowerCase this: 'GcC1zjxcYHe+cs92SQQTQRqd4Hc=' args: []
seq: 212 id: 114 func: call:toLowerCase res: 'gcc1zjxcyhe+cs92sqqtqrqd4hc='
seq: 213 id: 115 func: call:RegExp this: undefined args: ['=+$', '']
seq: 214 id: 115 func: call:RegExp res: /=+$/
seq: 215 id: 116 func: call:replace this: 'gcc1zjxcyhe+cs92sqqtqrqd4hc=' args: [/=+$/, '']
seq: 216 id: 116 func: call:replace res: 'gcc1zjxcyhe+cs92sqqtqrqd4hc'
seq: 217 id: 117 func: call:RegExp this: undefined args: ['[\\/+]', 'g']
seq: 218 id: 117 func: call:RegExp res: /[\/+]/g
seq: 219 id: 118 func: call:replace this: 'gcc1zjxcyhe+cs92sqqtqrqd4hc' args: [/[\/+]/g, '']
seq: 220 id: 118 func: call:replace res: 'gcc1zjxcyhecs92sqqtqrqd4hc'
seq: 221 id: 46 func: call:then state: fulfilled res: 'zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca'
seq: 222 id: 43 func: call:then state: fulfilled res: 'zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca'
zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca

```


重点观察这里:
```
seq: 103 id: 50 运算符: ^ args: [140,149] res: 25
seq: 104 id: 51 运算符: ^ args: [178,114] res: 192
seq: 105 id: 52 运算符: ^ args: [35,150] res: 181
seq: 106 id: 53 运算符: ^ args: [125,179] res: 206
seq: 107 id: 54 运算符: ^ args: [6,58] res: 60
seq: 108 id: 55 运算符: ^ args: [121,37] res: 92
seq: 109 id: 56 运算符: ^ args: [202,170] res: 96
seq: 110 id: 57 运算符: ^ args: [136,255] res: 119
seq: 111 id: 58 运算符: ^ args: [219,101] res: 190
seq: 112 id: 59 运算符: ^ args: [100,22] res: 114
seq: 113 id: 60 运算符: ^ args: [100,171] res: 207
seq: 114 id: 61 运算符: ^ args: [234,156] res: 118
seq: 115 id: 62 运算符: ^ args: [198,143] res: 73
seq: 116 id: 63 运算符: ^ args: [13,9] res: 4
seq: 117 id: 64 运算符: ^ args: [169,186] res: 19
seq: 118 id: 65 运算符: ^ args: [99,34] res: 65
seq: 119 id: 66 运算符: ^ args: [69,95] res: 26
seq: 120 id: 67 运算符: ^ args: [81,204] res: 157
seq: 121 id: 68 运算符: ^ args: [57,217] res: 224
seq: 122 id: 69 运算符: ^ args: [100,19] res: 119
```

 <8c b2 23 7d 06 79 ca 88 db 64 64 ea c6 0d a9 63 45 51 39 64>转10进制是:[140, 178, 35, 125, 6, 121, 202, 136, 219, 100, 100, 234, 198, 13, 169, 99, 69, 81, 57, 100]

列表a:[140, 178, 35, 125, 6, 121, 202, 136, 219, 100, 100, 234, 198, 13, 169, 99, 69, 81, 57, 100]

列表b:[149, 114, 150, 179, 58, 37, 170, 255, 101, 22, 171, 156, 143, 9, 186, 34, 95, 204, 217, 19]

列表c:[ 25, 192, 181, 206, 60, 92, 96, 119, 190, 114, 207, 118, 73, 4, 19, 65, 26, 157, 224, 119 ]

其实就是a^b = c

a是sha1("输入字符串")得到的20字节的10进制列表

b是xor掩码集

c就是中间段开头的20位数组

现在总结一下当前的进展:

1.中间段:开头的20位数组是怎么来的 (已解决)
2.开头段和结尾段:两组4个长度的列表是怎么来的. (已解决)
3.VMP环境检测:错误的环境导致错误的索引选择器 (待解决)

# 8.环境检测
现在虽然已经完整逆向了sign值的生成过程,但是生成的是假值,因为JSVMP对环境有检测.它肯定是检测到了环境不对.
证明生成的值是假值也很简单.在浏览器里打断点,调用**ie.getSecuritySign('12345').then(i=>console.log(i));**和node环境下我们得到的结果比较一下就好了.
![alt text](../posts/image/QQ音乐/image.png)
我们node环境里的值是:**zzc06238839gcc1zjxcyhecs92sqqtqrqd4hc510d64ca**
完全对不上.
所以现在生成的sign确实是假值.

我们继续看日志,注意这几个部分:
```
seq: 98 id: 48 func: call:u this: undefined args: [window]
seq: 99 id: 48 func: call:u res: 'object'
seq: 100 id: 49 func: call:u this: undefined args: [Navigator {}]
seq: 101 id: 49 func: call:u res: 'object'
seq: 102 id: 47 func: call:u res: 'FE'
```

```
seq: 42 id: 21 func: call:u res: { [Function: u] getInstance: [Function: u], kt: 'FingerprintModule' }
seq: 43 id: 22 func: call:u this: undefined args: []
seq: 44 id: 22 func: call:u res: { [Function: u] Ot: [Function: u], Bt: [ 'qq.com', 'joox.com', 'tencentmusic.com', 'wavecommittee.com', 'kugou.com', 'kuwo.cn' ] }
```

```
seq: 97 id: 47 func: call:u this: { [Function: u] Ot: [Function: u], Bt: [ 'qq.com', 'joox.com', 'tencentmusic.com', 'wavecommittee.com', 'kugou.com', 'kuwo.cn' ] } args: []
```

这里出现了window,navigator,域名列表.很有可能对这些进行了检测.

然后我们就针对浏览器常见的几大对象,慢慢补一下环境就行,最后也是出了真值了.

![alt text](../posts/image/QQ音乐/image-1.png)

和之前浏览器里的值做比较,完全一致.

sign完整的逆向过程就到此结束了.


其实这个接口一共有两个需要逆向的地方,一个是sign,一个是request payload.
但是request payload也是走的相同的JSVMP
![alt text](../posts/image/QQ音乐/image-2.png)

直接调用**re.encrypt('12345').then(i=>console.log(i))**就行.
这个方法返回的值是变化的，里面应该和时间戳有关.

# 9.总结
总结一下sign值的加密过程:

ie.getSecuritySign('12345')

**sign = 固定前缀 + 开头段 + 中间段 + 结尾段**


2.算法内部构建了一个环境检测的索引分配器,正确的索引分配器为:**[ 3, 1, 6, 17 ],[ 16, 12, 8, 5 ]**;错误的索引分配器为:**[ 4, 2, 7, 18 ], [ 17, 13, 9, 6 ]**.

3.JSVMP会检测运行环境是否为浏览器环境,如果检测发现异常,索引分配器全部+1,即:**[ 4, 2, 7, 18 ], [ 17, 13, 9, 6 ]**,这会取错误的数组下标元素,导致sign生成失败.

4.对20位数组调用索引分配器,产生两个4长度的数组;再对两组4个长度的列表里面的元素分别转16进制hex然后toString转字符串,然后再对它们补0
如果不需要补0就保持不变.
最终得出了两组16进制hex的列表,最后再对各自的列表join字符串得到**开头段和结尾段**

5.固定前缀位**zcc**不变

6.中间段:sha1生成的20字节数组转10进制和一个固定的掩码集做xor异或,生成一个20位的数组;对20位数组中的每一个元素做fromCharCode运算,然后join到一起,得到一长串鬼画符,然后通过btoa(一长串鬼画符)来得到一个字符串.

再通过两轮RegExp正则,替换掉字符串中的特殊符号,最终得到了**中间段**

7.最后把四段字符串拼接,就得到了sign值.

over.

后续再考虑对这个JSVMP内部的结构做更深入一层的挖掘.
