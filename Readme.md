docker run -p 8108:8108 -v/tmp/typesense-data:/data typesense/typesense:0.15.0 \
  --data-dir /data --api-key=12345