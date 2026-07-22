CREATE DATABASE IF NOT EXISTS astroos;

CREATE TABLE IF NOT EXISTS astroos.chart_features
(
    chart_id String,
    event_time DateTime64(3, 'UTC'),
    schema_version LowCardinality(String),
    feature_json String,
    provenance_json String
)
ENGINE = MergeTree
ORDER BY (chart_id, event_time);

CREATE TABLE IF NOT EXISTS astroos.hypotheses
(
    hypothesis_id String,
    created_at DateTime64(3, 'UTC'),
    status LowCardinality(String),
    statement String,
    metrics_json String,
    validation_json String
)
ENGINE = MergeTree
ORDER BY (hypothesis_id, created_at);
