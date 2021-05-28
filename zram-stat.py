#!/usr/bin/env python3
import argparse
import humanize
from termcolor import colored


def threshold(format_string: str, value: float, level_warning: float, level_critical: float):
    value_str = format_string.format(value)

    if value > level_critical:
        return colored(value_str, "red")
    elif value > level_warning:
        return colored(value_str, "yellow")
    else:
        return colored(value_str, "green")


def zram_stat():
    """
    Show statistics for zram devices
    """

    # parse arguments
    parser = argparse.ArgumentParser(description="Show Statistics for ZRAM Device")
    parser.add_argument("id", nargs="?", type=int, help="ZRAM Device ID", default=0)
    args = parser.parse_args()

    zram_id = args.id

    with open(f"/sys/block/zram{zram_id}/mm_stat", "r") as f:
        mm_stat = f.read()
        mm_stats = mm_stat.split()

    with open(f"/sys/block/zram{zram_id}/io_stat", "r") as f:
        io_stat = f.read()
        io_stats = io_stat.split()

    with open(f"/sys/block/zram{zram_id}/disksize", "r") as f:
        disksize = f.read().strip()

    with open(f"/sys/block/zram{zram_id}/max_comp_streams", "r") as f:
        max_comp_streams = f.read().strip()

    with open(f"/sys/block/zram{zram_id}/comp_algorithm", "r") as f:
        comp_algorithm = f.read().strip()

    memory_limit_percentage = (float(mm_stats[2]) / float(mm_stats[3])) * 100
    compressed_percentage = (float(mm_stats[1]) / float(mm_stats[0])) * 100
    disksize_used_percentage = (float(mm_stats[0]) / float(disksize)) * 100

    print(f"""{colored('General Statistics:', 'green')}
    Disk size: {humanize.naturalsize(disksize, binary=True)}
    Maximum compression streams: {max_comp_streams}
    Compression algorithm: {comp_algorithm}
""")

    print(f"""{colored('Memory Statistics:', 'green')}
    Original data size: {humanize.naturalsize(mm_stats[0], binary=True)} ({threshold('{0:.2f} %', disksize_used_percentage, 50, 75)})
    Compressed data size: {humanize.naturalsize(mm_stats[1], binary=True)} ({threshold('{0:.2f} %', compressed_percentage, 50, 75)})
    Memory used total: {humanize.naturalsize(mm_stats[2], binary=True)} ({threshold('{0:.2f} %', memory_limit_percentage, 50, 75)})
    Memory limit: {humanize.naturalsize(mm_stats[3], binary=True)}
    Memory used maximum: {humanize.naturalsize(mm_stats[4], binary=True)}
    Number of same element filled pages written: {mm_stats[5]}
    Number of pages freed during compaction: {mm_stats[6]}
    Number of incompressible pages: {mm_stats[7]}
""")

    print(f"""{colored('IO Statistics:', 'green')}
    Number of failed reads: {io_stats[0]}
    Number of failed writes: {io_stats[1]}
    Number of non-page-size-aligned I/O requests: {io_stats[2]}
    Number of pages freed: {io_stats[3]}
""")


if __name__ == "__main__":
    zram_stat()
