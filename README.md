# ZRAM Stat
Show statistics for zram devices

## Example Output

```
General Statistics:
    Disk size: 500.0 MiB
    Maximum compression streams: 4
    Compression algorithm: lzo lzo-rle [lz4] zstd

Memory Statistics:
    Original data size: 321.5 MiB (64.31 %)
    Compressed data size: 75.5 MiB (23.49 %)
    Memory used total: 79.5 MiB (39.77 %)
    Memory limit: 200.0 MiB
    Memory used maximum: 79.6 MiB
    Number of same element filled pages written: 8958
    Number of pages freed during compaction: 698
    Number of incompressible pages: 1188

IO Statistics:
    Number of failed reads: 0
    Number of failed writes: 0
    Number of non-page-size-aligned I/O requests: 0
    Number of pages freed: 131992
```
