{
  'variables': {
    'target_arch%': 'ia32', # default for node v0.6.x
    'node_major_version': '<!(node -e "console.log(process.versions.node.split(\'.\')[0])")'
  },

  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          },
        },
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, # static release
          },
        },
      }
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },

    'defines': [
      'LIBCOUCHBASE_INTERNAL=1',
      'LCB_LIBDIR=""'
    ],

    'include_dirs': [
      'include',
      'src',
      'contrib',
      'contrib/cbsasl/include',
      'gyp_config/common',
      'gyp_config/<(OS)/<(target_arch)'
    ],

    'conditions': [
      ['OS=="win"', {
        'include_dirs': [
          './',
          'contrib/win32-defs'
        ],
        "link_settings": {
          "libraries": [
            "-lws2_32.lib",
            "-ldnsapi.lib"
          ]
        }
      }],
    ]
  },

  'targets': [
    # libcbsasl
    {
      'target_name': 'cbsasl',
      'product_prefix': 'lib',
      'type': 'static_library',
      'defines': [
        'BUILDING_CBSASL'
      ],
      'sources': [
         'contrib/cbsasl/src/client.c',
         'contrib/cbsasl/src/common.c',
         'contrib/cbsasl/src/cram-md5/hmac.c',
         'contrib/cbsasl/src/cram-md5/md5.c',
         'contrib/cbsasl/src/hash.c'
      ]
    },

    # libcjson
    {
      'target_name': 'cjson',
      'product_prefix': 'lib',
      'type': 'static_library',
      'sources': [
        'contrib/cJSON/cJSON.c'
      ]
    },

    #libgenhash
    {
      'target_name': 'genhash',
      'product_prefix': 'lib',
      'type': 'static_library',
      'include_dirs': [
        './'
      ],
      'sources': [
        'contrib/genhash/genhash.c'
       ]
    },

    #libhttpparser
    {
      'target_name': 'httpparser',
      'product_prefix': 'lib',
      'type': 'static_library',
      'include_dirs': [
        './'
      ],
      'sources': [
        'contrib/http_parser/http_parser.c'
       ]
    },

    #libjsoncpp
    {
      'target_name': 'jsoncpp',
      'product_prefix': 'lib',
      'type': 'static_library',
      'sources': [
        'contrib/lcb-jsoncpp/lcb-jsoncpp.cpp'
       ],
    },

    #libsnappy
    {
      'target_name': 'snappy',
      'product_prefix': 'lib',
      'type': 'static_library',
      'sources': [
        'contrib/snappy/snappy-c.cc',
        'contrib/snappy/snappy-sinksource.cc',
        'contrib/snappy/snappy-stubs-internal.cc',
        'contrib/snappy/snappy.cc',
      ],
      'cflags': [
        '-Wno-sign-compare'
      ],
      'xcode_settings': {
        'WARNING_CFLAGS': [
          '-Wno-sign-compare'
        ]
      }
    },

    #libcouchbase
    {
      'target_name': 'couchbase',
      'product_prefix': 'lib',
      'type': 'static_library',
      'defines': [
        'CBSASL_STATIC'
      ],
      'cflags': [
        '-fno-strict-aliasing',
        '-Wno-missing-field-initializers'
      ],
      'cflags!': [
        '-fno-exceptions'
      ],
      'cflags_cc!': [
        '-fno-exceptions'
      ],
      'xcode_settings': {
        'WARNING_CFLAGS': [
          '-fno-strict-aliasing',
          '-Wno-missing-field-initializers'
        ],
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
      },
      'include_dirs': [
        './'
      ],
      'sources': [
        'src/bucketconfig/bc_cccp.cc',
        'src/bucketconfig/bc_file.cc',
        'src/bucketconfig/bc_http.cc',
        'src/bucketconfig/bc_static.cc',
        'src/bucketconfig/confmon.cc',
        'src/http/http.cc',
        'src/http/http_io.cc',
        'src/jsparse/parser.cc',
        'src/lcbht/lcbht.cc',
        'src/lcbio/connect.cc',
        'src/lcbio/ctx.c',
        'src/lcbio/iotable.c',
        'src/lcbio/ioutils.cc',
        'src/lcbio/manager.cc',
        'src/lcbio/protoctx.c',
        'src/lcbio/timer.c',
        'src/mc/compress.c',
        'src/mc/forward.c',
        'src/mc/mcreq.c',
        'src/mcserver/mcserver.cc',
        'src/mcserver/negotiate.cc',
        'src/n1ql/ixmgmt.cc',
        'src/n1ql/n1ql.cc',
        'src/n1ql/params.cc',
        'src/netbuf/netbuf.c',
        'src/operations/cbflush.cc',
        'src/operations/counter.cc',
        'src/operations/durability-cas.cc',
        'src/operations/durability-seqno.cc',
        'src/operations/durability.cc',
        'src/operations/get.cc',
        'src/operations/observe-seqno.cc',
        'src/operations/observe.cc',
        'src/operations/pktfwd.cc',
        'src/operations/ping.cc',
        'src/operations/remove.cc',
        'src/operations/stats.cc',
        'src/operations/store.cc',
        'src/operations/subdoc.cc',
        'src/operations/touch.cc',
        'src/rdb/bigalloc.c',
        'src/rdb/chunkalloc.c',
        'src/rdb/libcalloc.c',
        'src/rdb/rope.c',
        'src/strcodecs/base64.c',
        'src/vbucket/ketama.c',
        'src/vbucket/vbucket.c',
        'src/views/docreq.cc',
        'src/views/viewreq.cc',
        'src/auth.cc',
        'src/bootstrap.cc',
        'src/callbacks.c',
        'src/cbft.cc',
        'src/cntl.cc',
        'src/connspec.cc',
        'src/dns-srv.cc',
        'src/dump.cc',
        'src/errmap.cc',
        'src/getconfig.cc',
        'src/gethrtime.c',
        'src/handler.cc',
        'src/hashtable.c',
        ## 'src/hdr_timings.c',
        'src/hostlist.cc',
        'src/instance.cc',
        'src/iofactory.c',
        'src/legacy.c',
        'src/list.c',
        'src/logging.c',
        'src/newconfig.cc',
        'src/nodeinfo.cc',
        'src/retrychk.cc',
        'src/retryq.cc',
        'src/ringbuffer.c',
        'src/settings.c',
        'src/timings.c',
        'src/utilities.c',
        'src/wait.cc',

        'plugins/io/select/plugin-select.c'
      ],
      'dependencies': [
        'httpparser',
        'genhash',
        'cjson',
        'cbsasl',
        'snappy',
        'jsoncpp'
      ],
      'copies': [{
        'files': [ 'plugins/io/libuv/libuv_io_opts.h' ],
        'destination': 'include/libcouchbase/',
      }, {
        'files': [
          'plugins/io/libuv/plugin-libuv.c',
          'plugins/io/libuv/plugin-internal.h',
          'plugins/io/libuv/libuv_compat.h'
        ],
        'destination': 'include/libcouchbase/plugins/io/libuv/'
      }],
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
          './',
          'gyp_config/common',
          'gyp_config/<(OS)/<(target_arch)'
        ],
      },
      'conditions': [
        ['OS=="win"', {
          'sources': [
            'plugins/io/iocp/iocp_iops.c',
            'plugins/io/iocp/iocp_iops.h',
            'plugins/io/iocp/iocp_loop.c',
            'plugins/io/iocp/iocp_timer.c',
            'plugins/io/iocp/iocp_util.c'
          ],
          'direct_dependent_settings': {
            'include_dirs': [
              'plugins/io/libuv'
            ],
          },
        }],
		    ['OS!="win" or node_major_version>=6', {
          'sources': [
            'src/ssl/ssl_c.c',
            'src/ssl/ssl_common.c',
            'src/ssl/ssl_e.c',
          ]
        }],
		    ['OS=="win" and node_major_version<6', {
          'defines': [
            'LCB_NO_SSL'
          ]
        }]
      ]
    }
  ]
}
