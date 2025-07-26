if [ ! -s data/snapshots/*.snapshot ]; then
  echo "Snapshot missing - did you clone with Git LFS enabled?" >&2
  exit 1
fi