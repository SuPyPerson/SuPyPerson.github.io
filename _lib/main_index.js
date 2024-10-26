
  var num = 0;
  // mermaid.initialize({ startOnLoad: false });
    //var num = 0;
  //mermaid.initialize({ startOnLoad: false });

  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const release = urlParams.get('rel')

  let url = window.location.hostname; // obter o dominio
  let git = "https://raw.githubusercontent.com/SuPyPerson/SuPyPerson.github.io/";
  const thePaths ={i: "jaie24", o:"sbce", f:"guia", n:"snct", k:"pyjr", c:"snct/guia",
  j: git+"jaie24/jaie24/", p: git+"sbce/sbce", g:git+"jaie24/guia", m: git+"snct/snct", l: git+"pyjr"
  };
  let url_first = release //url[0];
  let docBasePath = "pyjr";
    // let url_name = url_splt[url_splt.length - 2];
  if ("cjklpgmiofn".indexOf(url_first) >= 0) {docBasePath = thePaths[url_first]; window.__SP_RELEASE__ = release;}
  console.log("got url to path", url_first, url, docBasePath, "cjklpgmiofn".indexOf(url_first) >= 0);


  window.$docsify = {
        // basePath: '/jaie24/',
        basePath: docBasePath,
        coverpage: ["/", "/jaie24/"],
        executeScript: false,
        accordify: {
            prerenderComments: true,                    // default
            selectors: ['h1','h2','h3','h4','h5','h6'], // default value
            debug: false,                               // default value
        },

      alias: {
        '/pyi/(.*)': '/pgintro/$1', // supports regexp
        '/pintro': '/pgintro/README',
        '/kwa': '/kwarwp/README',
        '/pyjr/(.*)': '/pyjr/$1',
        '/jaie24': '/README',
        '/soho': '/kwarwp/o_sonho',
        '/jardim': '/sbce/o_jogo',
        '/changelog':
          'https://raw.githubusercontent.com/docsifyjs/docsify/master/CHANGELOG',
        '/.*/_sidebar.md': '/_sidebar.md', // See #301
      },
    name: 'Pynoplia',
    nameLink: {
        // 'jaie24/': '#/jaie24/',
        '/': '#/',
      },
    // Sidebar Configuration
    auto2top: true,
    loadSidebar: true,
      mergeSidebar: true,
    // loadSidebar: './_sidebar.md',
    loadNavbar: true,
    maxLevel: 3,
    // Set subMaxLevel to 0 to remove automatic display of page table of contents (TOC) in Sidebar
    subMaxLevel: 2,
      sidebarDisplayLevel: 1,

    // Search Plugin Configuration
    search: {
    placeholder: 'Type to search',
    noData: 'No matches found.',
    // Headline depth, 1 - 6
    depth: 2,
    },
  };
