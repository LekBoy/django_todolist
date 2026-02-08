# empurrar um log manual para o Loki

curl -s -X POST "http://localhost:3100/loki/api/v1/push" \
  -H "Content-Type: application/json" \
  --data-raw '{
    "streams": [
      {
        "stream": {"app":"manual-test"},
        "values": [["'$(date +%s%N)'","hello from manual push"]]
      }
    ]
  }'

# no Grafana → Explore → Loki, pesquisa:
{app="manual-test"}
