#!/bin/bash
df / -h | grep root | awk '{ print $5 }'